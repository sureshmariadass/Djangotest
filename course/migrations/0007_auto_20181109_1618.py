# Generated by Django 2.0.4 on 2018-11-09 10:48

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20181018_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccategory', models.CharField(blank=True, max_length=250, null=True, unique=True, verbose_name='CoursesCategory')),
            ],
            options={
                'verbose_name': 'Courses Category',
                'verbose_name_plural': 'Courses Categories',
            },
        ),
        migrations.AlterField(
            model_name='coursedetails',
            name='courseid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.CourseId', verbose_name='CourseId'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coursedetails',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 9, 10, 48, 7, 621869, tzinfo=utc), null=True, verbose_name='Start Date'),
        ),
        migrations.AddField(
            model_name='coursedetails',
            name='ccategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.CoursesCategory', verbose_name='CoursesCategory'),
            preserve_default=False,
        ),
    ]