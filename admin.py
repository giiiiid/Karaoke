from django.contrib import admin
from .models import Authentication, Song, Artist
# Register your models here.
admin.site.register(Authentication)
admin.site.register(Song)
admin.site.register(Artist)
# admin.site.register(ArtistSong)