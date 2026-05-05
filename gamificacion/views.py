from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Quiz, Opcion, ResultadoQuiz, Cromo
from usuarios.models import Usuario, Notificacion

def lista_juegos(request):
    quizzes = Quiz.objects.all().order_by('id')
    completados_ids = []
    if request.user.is_authenticated:
        completados_ids = list(ResultadoQuiz.objects.filter(usuario=request.user).values_list('quiz_id', flat=True))
    
    quizzes_data = []
    unlocked = True
    for q in quizzes:
        is_completed = q.id in completados_ids
        quizzes_data.append({
            'quiz': q,
            'is_completed': is_completed,
            'is_unlocked': unlocked
        })
        # If this one is not completed, the next one will be locked
        if not is_completed:
            unlocked = False
    
    return render(request, 'gamificacion/lista_juegos.html', {
        'quizzes_data': quizzes_data
    })

def ranking(request):
    # Show all non-superuser registered users ordered by points
    usuarios = Usuario.objects.filter(is_superuser=False).order_by('-puntos_acumulados')
    return render(request, 'gamificacion/ranking.html', {'usuarios': usuarios})

@login_required(login_url='login')
def jugar_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    
    # Check if already played
    if ResultadoQuiz.objects.filter(usuario=request.user, quiz=quiz).exists():
        messages.info(request, f'Ya has completado el reto "{quiz.titulo}". ¡Prueba con otro!')
        return redirect('juegos_lista')

    # Check if it should be unlocked
    # For now, we assume quizzes must be completed in ID order
    quizzes = Quiz.objects.filter(id__lt=quiz.id)
    for pq in quizzes:
        if not ResultadoQuiz.objects.filter(usuario=request.user, quiz=pq).exists():
            messages.error(request, '¡Reto bloqueado! Debes completar los desafíos anteriores en orden.')
            return redirect('juegos_lista')

    preguntas = quiz.preguntas.all()
    
    if request.method == 'POST':
        puntos_ganados = 0
        total_preguntas = preguntas.count()
        correctas = 0
        
        for pregunta in preguntas:
            opcion_id = request.POST.get(f'pregunta_{pregunta.id}')
            if opcion_id:
                opcion = get_object_or_404(Opcion, id=opcion_id)
                if opcion.es_correcta:
                    puntos_ganados += 10
                    correctas += 1
        
        # Guardar resultado para evitar repetición
        ResultadoQuiz.objects.create(
            usuario=request.user,
            quiz=quiz,
            puntos=puntos_ganados
        )
        
        puntos_antes = request.user.puntos_acumulados
        
        # Update user points
        request.user.puntos_acumulados += puntos_ganados
        request.user.save()
        
        puntos_despues = request.user.puntos_acumulados
        
        # Detect if any cromo was unlocked in this session
        nuevos_cromos = Cromo.objects.filter(puntos_requeridos__gt=puntos_antes, puntos_requeridos__lte=puntos_despues)
        
        incorrectas = total_preguntas - correctas
        base_msg = f'¡Reto completado! ✅ Acertaste {correctas} y ❌ Fallaste {incorrectas}. Sumaste {puntos_ganados} puntos.'
        
        # Create general notification for quiz completion
        Notificacion.objects.create(
            usuario=request.user,
            mensaje=f'Completaste el reto "{quiz.titulo}" ganando {puntos_ganados} pts.',
            icono='fas fa-gamepad text-success'
        )

        if nuevos_cromos.exists():
            nombres = ", ".join([c.nombre for c in nuevos_cromos])
            base_msg += f' 🌟 ¡Felicidades! Has desbloqueado nuevas insignias para tu colección: {nombres}. ¡Revisa tus Insignias!'
            # Create specific notification for unlocked insignias
            Notificacion.objects.create(
                usuario=request.user,
                mensaje=f'¡Desbloqueaste nuevas insignias! Revisa tus Insignias para ver tus recompensas.',
                icono='fas fa-award text-warning'
            )
            
        messages.success(request, base_msg)
        return redirect('juegos_lista')
        
    return render(request, 'gamificacion/jugar_quiz.html', {'quiz': quiz, 'preguntas': preguntas})

@login_required(login_url='login')
def desafio_velocidad(request):
    top_user = Usuario.objects.filter(is_superuser=False).order_by('-puntos_acumulados').first()
    
    if request.method == 'POST':
        puntos = int(request.POST.get('puntos', 0))
        if puntos > 0:
            request.user.puntos_acumulados += puntos
            request.user.save()
            
            # Create Notification when points won in battle
            Notificacion.objects.create(
                usuario=request.user,
                mensaje=f'Sobreviviste al combate y ganaste {puntos} pts de Fama.',
                icono='fas fa-skull text-danger'
            )
            
            messages.success(request, f'¡Desafío superado! Ganaste {puntos} puntos por tu destreza.')
        return redirect('ranking')
        
    mode = request.GET.get('mode')
    if mode == 'synthwave':
        return render(request, 'gamificacion/desafio_synthwave.html', {'top_user': top_user})
    elif mode == 'undertale':
        return render(request, 'gamificacion/desafio_undertale.html', {'top_user': top_user})
    elif mode == 'cartas':
        return render(request, 'gamificacion/desafio_cartas.html', {'top_user': top_user})
    elif mode == 'ludo':
        return render(request, 'gamificacion/desafio_ludo.html', {'top_user': top_user})
    else:
        return render(request, 'gamificacion/desafio_seleccion.html', {'top_user': top_user})

@login_required(login_url='login')
def album_cromos(request):
    # Convertimos a lista para asegurar que el atributo dinámico "desbloqueado" se conserve en el template
    cromos = list(Cromo.objects.all().order_by('puntos_requeridos'))
    user_points = request.user.puntos_acumulados
    
    for c in cromos:
        c.desbloqueado = (user_points >= c.puntos_requeridos)
        
    return render(request, 'gamificacion/album.html', {
        'cromos': cromos,
        'user_points': user_points
    })
