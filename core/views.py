from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == "POST":

        return redirect('dashboard')
    return render(request, 'login.html')


def register_view(request):
    if request.method == "POST":

        return redirect('dashboard')
    return render(request, 'register.html')


def dashboard_view(request):
    return render(request, 'dashboard.html')