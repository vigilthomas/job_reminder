from django import forms
from joblisting.models import Category,Jobs


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=["name"]


class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        exclude = ["status"]
        widgets = {
            'category': forms.Select(attrs={"class": "form-select form-control "}),
        }