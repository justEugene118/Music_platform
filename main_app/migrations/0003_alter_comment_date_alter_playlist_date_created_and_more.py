# Generated by Django 4.0.4 on 2022-06-24 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_comment_date_alter_comment_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 23, 0, 57, 854072)),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 23, 0, 57, 853075)),
        ),
        migrations.AlterField(
            model_name='song',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 23, 0, 57, 852078)),
        ),
    ]
