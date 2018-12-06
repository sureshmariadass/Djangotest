from django.db import models

from django.utils.translation import ugettext as _
from django.utils import timezone

class Contact(models.Model):

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=100, blank=False)
    email = models.EmailField(max_length=70,blank=False, null= False)
    subject = models.CharField(
        verbose_name=_("Subject"),
        max_length=100, blank=True)
    messages = models.TextField(
        verbose_name=_("Messages"),
        blank=False,null=False)
    sent_date=models.DateTimeField(default=timezone.now(),
    null=True, blank=True,verbose_name=("Sent date"))

    def __str__(self):
        return self.name

# Create your models here.
