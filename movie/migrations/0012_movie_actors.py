# Generated by Django 4.1.2 on 2022-10-17 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_alter_actor_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movie_actors', to='movie.actor'),
        ),
    ]