# Generated by Django 4.1.2 on 2022-10-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0012_movie_actors'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(related_name='his_movies', to='movie.movie'),
        ),
    ]
