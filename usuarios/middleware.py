from django.shortcuts import redirect
from django.urls import resolve

class LoginRequiredMiddleware:
    """
    Middleware that requires a user to be authenticated to view any page other
    than login and registration.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info
        
        # Paths that ALWAYS require login
        if path.startswith('/juegos/quiz/'):
            if not request.user.is_authenticated:
                return redirect('login')
        
        # Default: Allow everything else
        return self.get_response(request)
