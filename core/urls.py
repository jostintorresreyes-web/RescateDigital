from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('proyecto/', views.proyecto, name='proyecto'),
    path('historia/', views.historia, name='historia'),
]
