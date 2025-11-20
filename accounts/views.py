from django.shortcuts import render, redirect

def register(request):
    return render(request, 'accounts/register.html')

def terms(request):
    return render(request, 'accounts/terms.html')

def privacy(request):
    return render(request, 'accounts/privacy.html')

def user_login(request):
    return render(request, 'accounts/login.html')

def password_reset(request):
    return render(request, 'accounts/forgot_password.html')