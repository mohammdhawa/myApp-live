# Generated by Django 4.1.2 on 2022-10-28 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0037_remove_season_series_season_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Series', to='movie.series'),
            preserve_default=False,
        ),
    ]
