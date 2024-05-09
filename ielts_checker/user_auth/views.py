from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, logout, login

from .forms import RegisterForm, LoginForm

def user_register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user-login')
    
    return render(request, 'register.html', {'form': form})

def user_login(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print('post: valid')
                return redirect('home-page')
    
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)

    return redirect('home-page')