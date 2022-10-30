# Generated by Django 4.1.2 on 2022-10-16 22:00

from django.db import migrations, models
import movie.models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_movie_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='image',
            field=models.ImageField(max_length=255, upload_to=movie.models.Actor.image_upload),
        ),
    ]