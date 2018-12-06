# Generated by Django 2.1.3 on 2018-12-04 07:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cantact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('subject', models.CharField(blank=True, max_length=100, verbose_name='Subject')),
                ('messages', models.TextField(verbose_name='Messages')),
                ('sent_date', models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 4, 7, 27, 23, 739572, tzinfo=utc), null=True, verbose_name='Sent date')),
            ],
        ),
    ]