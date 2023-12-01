from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Jobs(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    salary = models.PositiveIntegerField()
    experience = models.PositiveIntegerField(default=0)
    last_date = models.DateField()
    vaccancies = models.PositiveIntegerField(default=1)
    poster = models.ImageField(
        upload_to="static/poster_img", null=True, blank=True)
    contact = models.PositiveIntegerField()
    qualifications = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class StudentProfile(models.Model):
    qualifications = models.CharField(max_length=500)
    resume = models.FileField(
        upload_to="static/resumes", null=True, blank=True)
    skills = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    options = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others")
    )
    gender = models.CharField(max_length=100, choices=options, default="Male")
    experience = models.PositiveIntegerField(default=0)
    address = models.PositiveIntegerField()
    phone = models.PositiveIntegerField()
    profile_pic = models.ImageField(
        upload_to="static/profile_pic", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Applications(models.Model):
    jobs = models.ForeignKey(Jobs, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    applied_date = models.DateTimeField(auto_now=True)
    options = (
        ("Pending", "Pending"),
        ("Rejected", "Rejected"),
    )
    status = models.CharField(max_length=100, choices=options, default="Pend")


class Projects(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    git_link = models.CharField(max_length=1000)
    user=models.ForeignKey(StudentProfile,on_delete=models.DO_NOTHING)

    def  __str__(self):
        return self.name