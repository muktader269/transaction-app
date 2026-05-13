from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('email')
        p = request.POST.get('pin')
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        messages.error(request, "Invalid login!")
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        u = request.POST.get('email')
        p = request.POST.get('pin')
        if not User.objects.filter(username=u).exists():
            User.objects.create_user(username=u, password=p)
            return redirect('/')
        messages.error(request, "Already exists!")
    return render(request, 'register.html')

def dashboard_view(request):
    if not request.user.is_authenticated: return redirect('/')
    return render(request, 'dashboard.html')