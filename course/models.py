import re
import json
import csv
from django.db import models
from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.core.validators import MaxValueValidator, validate_comma_separated_integer_list
from django.utils.timezone import now
from django.conf import settings
from django.utils.translation import ugettext as _
from model_utils.managers import InheritanceManager
from django.utils import timezone

import io
from django.contrib.auth.models import User
from django.contrib import messages


class CourseIdManager(models.Manager):

    def new_courseid(self, courseid):
        new_courseid = self.create(courseid=re.sub('\s+', '-', courseid)
                                   .lower())

        new_courseid.save()
        return new_courseid


class CourseId(models.Model):

    courseid = models.CharField(
        verbose_name=_("CourseId"),
        max_length=250, blank=True,
        unique=True, null=True)

    objects = CourseIdManager()

    class Meta:
        verbose_name = _("CourseId")
        verbose_name_plural = _("CourseId's")

    def __str__(self):
        return self.courseid


class CategoryManager(models.Manager):

    def new_category(self, category):
        new_category = self.create(category=re.sub('\s+', '-', category)
                                   .lower())

        new_category.save()
        return new_category




class Category(models.Model):

    category = models.CharField(
        verbose_name=_("Category"),
        max_length=250, blank=True,
        unique=True, null=True)
    objects = CategoryManager()

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.category



class CourseDetails(models.Model):

    category=models.ForeignKey(Category,null=True,blank=True,max_length=250,verbose_name=_("Category"),on_delete=models.CASCADE)

    name = models.CharField(
        verbose_name=_("Course Name"),
        max_length=60, blank=False)

    courseid = models.ForeignKey(
        CourseId, null=True, blank=True,
        verbose_name=_("CourseId"), on_delete=models.CASCADE)

    image=models.ImageField(upload_to='course_image',blank=False,verbose_name=_("Course Thumbnail"))

    start_date=models.DateTimeField(default=timezone.now(),
    null=True, blank=True,verbose_name=("Start Date"))

    end_date=models.DateTimeField(null=True, blank=True,
    verbose_name=("End Date"))

    description = models.TextField(
        verbose_name=_("Course Description"),
        blank=True, help_text=_("a description of the Course"))

    url = models.SlugField(
        max_length=60, blank=False,
        help_text=_("a user friendly url"),
        verbose_name=_("user friendly url"))

    course_requirements = models.TextField(
        blank=True, help_text=_("Course requirements."),
        verbose_name=_("Course requirements"))

    target_audience= models.TextField(
        verbose_name=_("Target Audience"),
        blank=True, help_text=_("Who need this course?"))

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.url = re.sub('\s+', '-', self.url).lower()

        self.url = ''.join(letter for letter in self.url if
                           letter.isalnum() or letter == '-')


        super(CourseDetails, self).save(force_insert, force_update, *args, **kwargs)

    class Meta:
        verbose_name = _("CourseDetails")
        verbose_name_plural = _("CourseDetails")

    def __str__(self):
        return self.name

    # def __str__(self):
    #     return self.courseid

    def get_url(self):
        return reverse(detail,args=[self.id,self.url])

class CourseContent(models.Model):

    sub_title = models.CharField(
        verbose_name=_("Sub title"),
        max_length=100, blank=False)

    courseid = models.ForeignKey(
        CourseId, null=True, blank=True,
        verbose_name=_("CourseId"), on_delete=models.CASCADE)

    video = models.FileField(upload_to="videos",verbose_name=_("Course video"))

    explain = models.TextField(
        verbose_name=_("Video Description"),
        blank=True, help_text=_("a description of the video"))

    class Meta:
        verbose_name = _("CourseContent")
        verbose_name_plural = _("CourseContents")

    def get_absolute_url(self):
        return reverse(cour, args=[self.courseid])




class Question(models.Model):


    courseid = models.ForeignKey(
        CourseId, null=True, blank=True,
        verbose_name=_("CourseId"), on_delete=models.CASCADE)

    question=models.CharField(max_length=300, verbose_name=_("Question"),blank=False, null=False)

    option1 = models.CharField(
        verbose_name=_("A"),
        max_length=60, blank=False, null=False)
    option2 = models.CharField(
            verbose_name=_("B"),
            max_length=60, blank=False, null=False)
    option3 = models.CharField(
                verbose_name=_("C"),
                max_length=60, blank=False, null=False)
    option4 = models.CharField(
        verbose_name=_("D"),
        max_length=60, blank=False, null=False)


    answer = models.CharField(
        verbose_name=_("answer"),
        max_length=60, blank=False, null=False)
    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
class Progress(models.Model):

    user=models.CharField(verbose_name=_("User"),
    max_length=60)
    date=models.DateTimeField(default=timezone.now(),
    null=True, blank=True,verbose_name=("Date"))
    cid=models.CharField(verbose_name=_("CourseId"),
    max_length=60)
    correct=models.CharField(verbose_name=_("Score"),null=True, blank=True,
    max_length=60)
    total=models.CharField(verbose_name=_("Possible Score"),
    max_length=60)
