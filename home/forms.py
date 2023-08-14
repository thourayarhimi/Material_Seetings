from django import forms

from .models import FileMs,rute


class mara_marc(forms.Form):
    class meta:
     model = FileMs
    fields = '__all__'
 

class RuleForm(forms.ModelForm):
    class Meta:
        model = rute
        fields = ['name']   
 