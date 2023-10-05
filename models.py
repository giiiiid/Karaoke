from django.db import models

# Create your models here.
class Authentication(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Song(models.Model):
    artiste = models.CharField(max_length=150)
    song_name = models.CharField(max_length=150)
    cover_image = models.ImageField(upload_to='cover_images')
    audio_file = models.FileField(upload_to='audios')

    def __str__(self):
        return self.artiste + '-' + self.song_name