from django import forms
import re 
from .models import mara_marc_for_MS
from .models import Rule

class mara_marc(forms.Form):
    class meta:
        model= mara_marc_for_MS
        fields='_all_'
 
 

class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ('rule_name', 'comment')    