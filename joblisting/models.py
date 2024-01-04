from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Jobs(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    salary = models.PositiveIntegerField()
    experience = models.PositiveIntegerField(default=0)
    last_date = models.DateField()
    vaccancies = models.PositiveIntegerField(default=1)
    poster = models.ImageField(upload_to="posterimages", null=True, blank=True)
    contact = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)
    company = models.CharField(max_length=200,null=True)
    options = (
        ("Part-time", "Part-time"),
        ("Full-time", "Full-time")
    )
    job_type = models.CharField(
        max_length=200, choices=options, default="full-time")

    def __str__(self) -> str:
        return self.title
        
    def application_count(self):
        qs=Applications.objects.filter(job=self).count()
        return qs


class StudentProfile(models.Model):
    qualification = models.CharField(max_length=200)
    resume = models.FileField(upload_to="resumes", null=True, blank=True)
    skills = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    options = (
        ("Male", "Male"), ("Female", "Female"), ("Others", "Others"),
    )
    gender = models.CharField(max_length=200, choices=options, default="Male")
    experience = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    profile_pic = models.ImageField(
        upload_to="profilepics", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    saved_job = models.ManyToManyField(Jobs, null=True, related_name="saved")


class Applications(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    applied_date = models.DateTimeField(auto_now_add=True)
    options = (
        ("pending", "pending"), ("rejected", "rejected"), ("processing", "processing")
    )
    status = models.CharField( max_length=200, choices=options, default="pending")


class Projects(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    git_link = models.CharField(max_length=200)
    user = models.ForeignKey(StudentProfile, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name