from django.contrib import admin
from .models import Authentication, Song, Artist, Favourite
# Register your models here.
admin.site.register(Authentication)
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Favourite)
# admin.site.register(ArtistSong)