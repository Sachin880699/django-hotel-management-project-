from django import forms
from.models import *

class Reserveform(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = "__all__"