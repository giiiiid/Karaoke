from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Authentication(models.Model):
    # user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Artist(models.Model):
    # artiste_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, default=False)
    description = models.TextField(max_length=10000)
    
    def save(self, *args, **kwargs):
        super(Artist, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name


class Song(models.Model):
    # song_id = models.AutoField(primary_key=True)
    name = models.ForeignKey(Artist, on_delete=models.CASCADE, default=True)
    artiste = models.CharField(max_length=150)
    song_name = models.CharField(max_length=150)
    cover_image = models.ImageField(upload_to='cover_images')
    audio_file = models.FileField(upload_to='audios')
    genre = models.CharField(max_length=100, null=False, default=True)
    producer = models.CharField(max_length=100, null=False, default=True)

    def __str__(self):
        return self.artiste + '-' + self.song_name


class Favourite(models.Model):
    # fav_song_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fav_id = models.CharField(max_length=10000, default='')