from django import forms
import re 
from .models import mara_marc_for_MS


class mara_marc(forms.Form):
    class meta:
        model= mara_marc_for_MS
        fields='_all_'
       