from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from jobseeker.views import *

urlpatterns = [
    path('register/', SignUpView.as_view(), name="jobseeker_signup"),
    path('index/', JobseekerIndex.as_view(), name="jobseeker_home"),
    path('addprofile/', ProfileCreateView.as_view(), name="jobseeker_addprofile"),
    path('detailprofile/<int:pk>/view', ProfileDetailView.as_view(), name="jobseeker_detailprofile"),
    path('editprofile/<int:pk>/edit', ProfileUpdateView.as_view(), name="jobseeker_editprofile"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
