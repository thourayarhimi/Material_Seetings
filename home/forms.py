from django import forms

from django.contrib.auth.models import User


from .models import FileMs,rute,EquipeMS


class mara_marc(forms.Form):
    class meta:
     model = FileMs
    fields = '__all__'
 

class RuleForm(forms.ModelForm):
    class Meta:
        model = rute
        fields = ['name']  
        
        
class Equipeform(forms.ModelForm):
    class Meta:
        model = EquipeMS
        fields = ['name','email','Phone'] 
        

 