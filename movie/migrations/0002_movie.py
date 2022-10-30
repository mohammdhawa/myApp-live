# Generated by Django 4.1.2 on 2022-10-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('country', models.CharField(choices=[('US', 'US'), ('UK', 'UK'), ('Canada', 'Canada'), ('Japan', 'Jaban'), ('Kore', 'Kore'), ('Turkey', 'Turkey')], max_length=50)),
                ('running_time', models.IntegerField()),
                ('type', models.ManyToManyField(related_name='movie_type', to='movie.movietype')),
            ],
        ),
    ]
