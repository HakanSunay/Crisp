# Generated by Django 2.0.7 on 2018-07-30 10:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 7, 30, 10, 55, 50, 169763, tzinfo=utc)),
            preserve_default=False,
        ),
    ]