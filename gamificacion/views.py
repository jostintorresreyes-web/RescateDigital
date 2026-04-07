from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Quiz, Opcion, ResultadoQuiz
from usuarios.models import Usuario

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
        
        # Update user points
        request.user.puntos_acumulados += puntos_ganados
        request.user.save()
        
        incorrectas = total_preguntas - correctas
        messages.success(request, f'¡Reto completado! ✅ Acertaste {correctas} y ❌ Fallaste {incorrectas}. Sumaste {puntos_ganados} puntos.')
        return redirect('juegos_lista')
        
    return render(request, 'gamificacion/jugar_quiz.html', {'quiz': quiz, 'preguntas': preguntas})
