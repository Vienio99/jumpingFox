# Generated by Django 3.1.5 on 2021-01-18 11:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 11, 26, 13, 166112, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default='Unknown', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
