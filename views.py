from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import AddSongForms
from .models import Song, Artist, Favourite
from .decorators import unauthorised_user, can_add_song
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required(redirect_field_name='login', login_url='login')
def artist(request, id):
    songs = Song.objects.get(id=id)
    artiste = Artist.objects.get(id=id)
    return render(request, 'artist.html', {'songs':songs, 'artiste':artiste})


@login_required(redirect_field_name='login', login_url='login')
def blog(request):
    return render(request, 'blog.html')


@login_required(redirect_field_name='login', login_url='login')
def category(request):
    songs = Song.objects.all()
    return render(request, 'category.html', {'songs':songs})


@login_required(redirect_field_name='login', login_url='login')
def playlist(request):
    return render(request, 'playlist.html')


# @login_required(redirect_field_name='login', login_url='login')
def fav(request):
    if request.method == 'POST':
        user = request.user
        fav_id = request.POST['fav_id']

        if Favourite.objects.filter(fav_id=fav_id).exists():
            Favourite.objects.exclude(fav_id=fav_id)
        else:
            favis = Favourite(user=user, fav_id=fav_id)
            favis.save()
        return redirect('fav')

    else:
        favs = Favourite.objects.all()
    
    return render(request, 'fav.html', {'favs':favs})

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
        password_1 = request.POST['password1']
        password_2 = request.POST['password2']

        if password_1 == password_2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, password=password_1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords don't match")
            return redirect('create')
    return render(request, 'create.html')


@unauthorised_user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is None:
            messages.info(request, 'User does not exist')
            return redirect('login')
        else:
            auth.login(request, user)
            return redirect('home')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


@can_add_song(allowed_users=[])
def add(request):
    forms = AddSongForms()
    if request.method == 'POST':
        forms = AddSongForms(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    context = {'forms':forms}
    return render(request, 'add.html', context)