from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
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
    # with mail.get_connection() as connection:
    #     mail.EmailMessage(
    #         subject,
    #         message,
    #         email,
    #         [settings.EMAIL_HOST_USER],
    #         connection=connection,
    #     ).send()
    return render(request, 'contact.html')