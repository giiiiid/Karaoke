# Generated by Django 4.2.2 on 2023-10-07 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karaoke', '0010_remove_artist_main_remove_song_id_song_artist_ptr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(default=True, max_length=150),
        ),
    ]