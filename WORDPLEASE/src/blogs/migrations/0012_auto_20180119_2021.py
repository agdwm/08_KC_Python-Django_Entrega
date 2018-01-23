# Generated by Django 2.0.1 on 2018-01-19 20:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_auto_20180116_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='release_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
