from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from jobseeker.views import *

urlpatterns = [
    path('register/', SignUpView.as_view(), name="jobseeker_signup"),
    path('index/', JobseekerIndex.as_view(), name="jobseeker_home"),
    path('jobdetail/<int:pk>', JobDetailView.as_view(),name="jobseeker_jobdetail"),
    path('addprofile/', ProfileCreateView.as_view(), name="jobseeker_addprofile"),
    path('detailprofile/<int:pk>/view', ProfileDetailView.as_view(), name="jobseeker_detailprofile"),
    path('editprofile/<int:pk>/edit', ProfileUpdateView.as_view(), name="jobseeker_editprofile"),
    path('job/<int:pk>/apply', ApplyJobView.as_view(),name="jobseeker_applyjob"),
    path('job/applied_jobs/', ApplicationListView.as_view(),name="jobseeker_appliedjob"),
    path('job/save_jobs/<int:pk>', SaveJobView.as_view(),name="savejob"),
    path('job/savedjob/<int:pk>', SavedJobListView.as_view(), name="savedjobs"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
