from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home', views.home, name='home'),
    path('artist/<str:id>', views.artist, name='artist'),
    path('blog', views.blog, name='blog'),
    path('category', views.category, name='category'),
    path('playlist', views.playlist, name='playlist'),
    path('contact', views.contact, name='contact'),
    path('create', views.create, name='create'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
