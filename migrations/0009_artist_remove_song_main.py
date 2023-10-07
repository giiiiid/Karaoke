# Generated by Django 4.2.2 on 2023-10-07 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karaoke', '0008_song_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=False, max_length=150)),
                ('description', models.TextField(default=False, max_length=10000)),
                ('main', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='main',
        ),
    ]