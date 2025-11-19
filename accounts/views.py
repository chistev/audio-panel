from django.shortcuts import render, redirect

def register(request):
    return render(request, 'accounts/register.html')

def terms(request):
    return render(request, 'accounts/terms.html')

def privacy(request):
    return render(request, 'accounts/privacy.html')