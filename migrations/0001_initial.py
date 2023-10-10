# Generated by Django 4.2.2 on 2023-10-10 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artiste_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=False, max_length=150)),
                ('description', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('artiste', models.CharField(max_length=150)),
                ('song_name', models.CharField(max_length=150)),
                ('cover_image', models.ImageField(upload_to='cover_images')),
                ('audio_file', models.FileField(upload_to='audios')),
                ('genre', models.CharField(default=True, max_length=100)),
                ('producer', models.CharField(default=True, max_length=100)),
                ('name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='karaoke.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('fav_song_id', models.AutoField(primary_key=True, serialize=False)),
                ('fav_id', models.CharField(default='', max_length=10000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
