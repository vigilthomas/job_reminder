from django.views.generic import View, FormView, TemplateView, CreateView,ListView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.urls import reverse_lazy

from hr.forms import *
from joblisting.models import Category

# Create your views here.


# class SigninView(View):
class SigninView(FormView):
    template_name = "hr/login.html"
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user_obj = authenticate(request, username=uname, password=pwd)
            if user_obj:
                login(request, user_obj)
                print("Success")
                return redirect('hr_home')
        print("Failed")
        return render(request,"hr/login.html",{"form":form})

class SignoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        print("logout")
        return redirect('hr_login')

class IndexView(TemplateView):
    template_name="hr/index.html"


class CategoryCreateListView(CreateView,ListView):
    template_name = "hr/category.html"
    form_class = CategoryForm
    success_url = reverse_lazy("hr_category")
    context_object_name="data"
    model=Category

class CatDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Category.objects.filter(id=id).delete()
        return redirect("hr_category")

class JobAddView(CreateView):
    template_name = "hr/addjob.html"
    form_class = JobForm
    success_url = reverse_lazy("list_job")

class JobListView(ListView):
    template_name = "hr/listjob.html"
    context_object_name = "data"
    model = Jobs
