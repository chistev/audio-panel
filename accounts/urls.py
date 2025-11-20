from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('password-reset/', views.password_reset, 
         name='password_reset'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
]