from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from joblisting.models import StudentProfile

class RegisterForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=["username","email","password1","password2"]


class ProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile
        exclude = ("user",)
        widgets = {
            'qualification': forms.TextInput(attrs={"class": "col-lg-6 col-md-6 col-sm-12 col-12 form-control "}),
            'resume': forms.FileInput(attrs={"class": "col-lg-6 col-md-6 col-sm-12 col-12 form-control "}),
            'skills': forms.Textarea(attrs={"class": "col-lg-6 col-md-6 col-sm-12 col-12 form-control","row":"3"}),
            'age': forms.TextInput(attrs={"class": "col-lg-6 col-md-6 col-sm-12 col-12 form-control " }),
            'gender': forms.Select(attrs={"class": "col-lg-6 col-md-6 col-sm-12 col-12 form-select form-control "}),
            'experience': forms.TextInput(attrs={"class": "col-lg-6 col-md-6 col-sm-12 col-12 form-control "}),
            'address': forms.TextInput(attrs={"class": "col-lg-6 col-md-6 col-sm-12 col-12 form-control "}),
            'phone': forms.TextInput(attrs={"class": "col-lg-6 col-md-6 col-sm-12 col-12 form-control "}),
            'profile_pic': forms.FileInput(attrs={"class": "col-lg-6 col-md-6 col-sm-12 col-12 form-control "}),

        }
