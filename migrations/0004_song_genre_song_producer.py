# Generated by Django 4.2.2 on 2023-10-06 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karaoke', '0003_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='song',
            name='producer',
            field=models.CharField(default=True, max_length=100),
        ),
    ]