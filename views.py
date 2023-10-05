from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import AuthenticationForms
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html')

def artist(request):
    return render(request, 'artist.html')

def blog(request):
    return render(request, 'blog.html')

def category(request):
    return render(request, 'category.html')

def playlist(request):
    return render(request, 'playlist.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(subject,message,email,[settings.EMAIL_HOST_USER])
    
    return render(request, 'contact.html')

def create(request):
    if request.method == 'POST':
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']

        if password_1 == password_2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords don't match")
            return redirect('create')
    return render(request, 'create.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passed = request.POST['password']
        user = auth.authenticate(username=username, password=passed)

        if user is None:
            messages.info(request, 'User does not exist')
        else:
            auth.login(request, user)
            return redirect('home')
    else:
        return render(request, 'login.html')