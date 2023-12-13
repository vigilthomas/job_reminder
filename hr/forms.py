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
            'category': forms.Select(attrs={"class": "col-lg-6 col-md-6 col-sm-12 col-12 form-select form-control "}),
            "last_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }


class JobChangeForm(forms.ModelForm):

    class Meta:
        model = Jobs
        fields = "__all__"
        widgets = {
            'category': forms.Select(attrs={"class": "col-lg-6 col-md-6 col-sm-12 col-12 form-select form-control "}),
            "last_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
