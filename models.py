from django.db import models

# Create your models here.
class Authentication(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Artist(models.Model):
    name = models.CharField(max_length=150, default=True)
    description = models.TextField(max_length=10000)
    
    def save(self, *args, **kwargs):
        super(Artist, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.ForeignKey(Artist, on_delete=models.CASCADE, default=True)
    artiste = models.CharField(max_length=150)
    song_name = models.CharField(max_length=150)
    cover_image = models.ImageField(upload_to='cover_images')
    audio_file = models.FileField(upload_to='audios')
    genre = models.CharField(max_length=100, null=False, default=True)
    producer = models.CharField(max_length=100, null=False, default=True)
    
    def __str__(self):
        return self.artiste + '-' + self.song_name


