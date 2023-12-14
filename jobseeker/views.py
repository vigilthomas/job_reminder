from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,DetailView,UpdateView,ListView

from jobseeker.forms import RegisterForm,ProfileForm
from joblisting.models import StudentProfile,Jobs
# Create your views here.


class SignUpView(CreateView):
    template_name="jobseeker/register.html"
    form_class = RegisterForm
    success_url=reverse_lazy("hr_login")

class JobseekerIndex(ListView):
    template_name = "jobseeker/index.html"
    context_object_name = "data"
    model = Jobs

    def get(self, request, *args, **kwargs):
        qs1 = Jobs.objects.all()
        qs2 = StudentProfile.objects.get(user=request.user)

        if "status" in request.GET:
            qs = qs.filter(status=True)
        return render(request, self.template_name,{"data":qs1,"ud":qs2})


class ProfileCreateView(CreateView):
    template_name = "jobseeker/addprofile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("jobseeker_home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    

class ProfileDetailView(DetailView):
    template_name = "jobseeker/detailprofile.html"
    context_object_name = "data"
    model = StudentProfile


class ProfileUpdateView(UpdateView):
    template_name = "jobseeker/editprofile.html"
    model = StudentProfile
    form_class=ProfileForm
    success_url=reverse_lazy("jobseeker_home")

