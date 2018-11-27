from django import forms
from .models import Progress


class ProgressForm(forms.Form):
    user=forms.CharField()
    cid=forms.CharField()
    correct=forms.CharField()
    total=forms.CharField()

    class Meta(object):
        model=Progress
