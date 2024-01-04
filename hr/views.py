from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import View, FormView, TemplateView, CreateView,ListView,UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.urls import reverse_lazy

from hr.forms import *
from joblisting.models import Category,Applications

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
                if request.user.is_superuser:
                    return redirect("hr_home")
                else:
                    return redirect("jobseeker_home")
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

    def get(self,request,*args,**kwargs):
        qs=Jobs.objects.all()

        if "status" in request.GET:
            value=request.GET.get("status")
            qs=qs.filter(status=value)
        return render(request,self.template_name,{"data":qs})

    # def get_queryset(self):
    #     return Jobs.objects.filter(status=True)


class JobCompleteView(ListView):
    template_name = "hr/listjob.html"
    context_object_name = "data"
    model = Jobs

    def get_queryset(self):
        return Jobs.objects.filter(status=False)

class JobDeleteView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        Jobs.objects.filter(id=id).delete()
        return redirect("list_job")


class JobUpdateView(UpdateView):
    form_class = JobChangeForm
    template_name = "hr/updatejob.html"
    model=Jobs
    success_url = reverse_lazy("list_job")


class JobApplicationListView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        # job_id = Jobs.objects.get(id=id)
        qs = Applications.objects.filter(job=id)
        return render(request, "hr/applications.html", {"data": qs})








    