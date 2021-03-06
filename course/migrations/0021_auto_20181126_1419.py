# Generated by Django 2.1.3 on 2018-11-26 08:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0020_auto_20181126_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedetails',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 26, 8, 49, 16, 88101, tzinfo=utc), null=True, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 26, 8, 49, 16, 91101, tzinfo=utc), null=True, verbose_name='Date'),
        ),
    ]
