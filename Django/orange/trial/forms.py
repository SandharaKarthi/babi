from django import forms
from trial.models import employee_details

class f1(forms.Form):
    Name = forms.CharField(max_length=50)
    DOB = forms.DateField
    phone = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    re_password = forms.CharField(max_length=50)

def clean(self):
    a = super().clean()
    pwd = a['password']
    r_pwd = a['re_password']
           
    if pwd != r_pwd:
        raise forms.ValidationError('kindly enter same password')

class f2(forms.ModelForm):
    class Meta:
        model = employee_details
        fields = "__all__"


 
 
 
 
 
            
            