# Generated by Django 4.2.2 on 2023-10-09 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karaoke', '0018_alter_song_song_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='id',
        ),
        migrations.AddField(
            model_name='favourite',
            name='fav_song_id',
            field=models.AutoField(default='', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]