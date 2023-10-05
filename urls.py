from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('artist', views.artist, name='artist'),
    path('blog', views.blog, name='blog'),
    path('category', views.category, name='category'),
    path('playlist', views.playlist, name='playlist'),
    path('contact', views.contact, name='contact')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
