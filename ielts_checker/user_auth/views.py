from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, logout, login

from .models import UserProfile
from .forms import RegisterForm, LoginForm, UserForm, UserProfileForm

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

def profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile if hasattr(request.user, 'userprofile') else UserProfile.objects.create(user=request.user))
        # print(request.POST.get('first_name'))
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    if request.method == 'GET':
        user_id = int(request.GET.get('user_id'))
        user = User.objects.get(id=user_id)

        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=user.userprofile if hasattr(request.user, 'userprofile') else UserProfile.objects.create(user=request.user))

        if request.user != user:
            for field in user_form.fields.values():
                field.widget.attrs['disabled'] = 'disabled'
            for field in profile_form.fields.values():
                field.widget.attrs['disabled'] = 'disabled'
    return render(request, 'profile.html', context={'user_form': user_form, 'profile_form': profile_form, 'user': user})