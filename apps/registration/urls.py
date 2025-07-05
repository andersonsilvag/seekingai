from django.urls import path
from .views import signup_view

app_name = 'registration'  # Define o nome do aplicativo
urlpatterns = [
    path('register/', signup_view, name='signup'),
    
]