from django import forms 
from django.contrib.auth.models import User
from .models import *

class Registerform(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username','first_name','last_name','password']
    


class Userform(forms.ModelForm):
    class Meta:
        model = Owner 
        fields = ('username','first_name','last_name','password')
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
            # 'manager': forms.Select(attrs={'class':'form-select'})
        }

class Blogsform(forms.ModelForm):
    class Meta:
        model = Blogs 
        fields = ('name','title','image')
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            # 'manager': forms.Select(attrs={'class':'form-select'})
        }