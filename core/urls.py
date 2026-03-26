from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('historia/', views.historia, name='historia'),
]
