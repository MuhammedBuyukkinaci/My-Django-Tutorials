# Generated by Django 2.1.5 on 2021-03-13 10:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210313_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 13, 10, 14, 12, 972879, tzinfo=utc), verbose_name='date published'),
        ),
    ]