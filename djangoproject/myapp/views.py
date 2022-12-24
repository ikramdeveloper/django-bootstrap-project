from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def home(request):
    context = {
        'features': Feature.objects.all()
    }
    return render(request, 'index.html', context)

def register(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']
        
        if password != confirm_password:
            messages.info(request, 'Passwords do not match')
            return redirect('/register')

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists')
            return redirect('/register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'username already taken')
            return redirect('/register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('/login')
    

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is None:
            messages.info(request, 'Invalid username or password')
            return redirect('/login')

        auth.login(request, user)
        return redirect('/')
            
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def user(request, username):
    context = {
        'username': username
    }
    
    if request.user.is_authenticated:
        context['email'] = request.user.email
    
    return render(request, 'user.html', context)