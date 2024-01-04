from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, TemplateView, DetailView, UpdateView, ListView

from jobseeker.forms import RegisterForm, ProfileForm
from joblisting.models import StudentProfile, Jobs, Applications
# Create your views here.


class SignUpView(CreateView):
    template_name = "jobseeker/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("hr_login")


class JobseekerIndex(ListView):
    template_name = "jobseeker/index.html"
    context_object_name = "data"
    model = Jobs

    def get_queryset(self):
        my_applications = Applications.objects.filter(
            student=self.request.user).values_list("job", flat=True)
        qs = Jobs.objects.exclude(id__in=my_applications)
        return qs


class JobDetailView(DetailView):
    template_name = "jobseeker/job_detail.html"
    context_object_name = "data"
    model = Jobs


class ProfileCreateView(CreateView):
    template_name = "jobseeker/addprofile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("jobseeker_home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileDetailView(DetailView):
    template_name = "jobseeker/detailprofile.html"
    context_object_name = "data"
    model = StudentProfile


class ProfileUpdateView(UpdateView):
    template_name = "jobseeker/editprofile.html"
    model = StudentProfile
    form_class = ProfileForm
    success_url = reverse_lazy("jobseeker_home")


class ApplyJobView(View):
    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        job_obj = Jobs.objects.get(id=id)
        student_obj = request.user
        Applications.objects.create(job=job_obj, student=student_obj)
        return redirect("jobseeker_home")


class ApplicationListView(ListView):
    template_name = "jobseeker/applied.html"
    context_object_name = "data"
    model = Applications

    def get_queryset(self):
        qs = Applications.objects.filter(student=self.request.user)
        return qs


class SaveJobView(View):
    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        job_obj = Jobs.objects.get(id=id)
        action = request.POST.get("action")
        print(action)
        print(request.user.profile.saved_job.all())
        if action == "save":
            request.user.profile.saved_job.add(job_obj)
        elif action == "unsave":
            request.user.profile.saved_job.remove(job_obj)
        return redirect('jobseeker_home')


class SavedJobListView(View):
    template_name = "jobseeker/savedjob.html"
    model = StudentProfile

    def get(self, request,*args, **kwargs):
        qs=request.user.profile.saved_job.all()
        return render(request, self.template_name,{"data":qs})
