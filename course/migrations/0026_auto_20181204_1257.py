# Generated by Django 2.1.3 on 2018-12-04 07:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0025_auto_20181126_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedetails',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 4, 7, 27, 23, 726572, tzinfo=utc), null=True, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 4, 7, 27, 23, 729572, tzinfo=utc), null=True, verbose_name='Date'),
        ),
    ]
