# Generated by Django 3.1.5 on 2021-01-18 11:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210118_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 11, 33, 34, 896558, tzinfo=utc), verbose_name='date published'),
        ),
    ]
