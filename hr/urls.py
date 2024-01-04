from django.urls import path

from hr.views import *

urlpatterns = [
    path('', SigninView.as_view(), name="hr_login"),
    path('logout/', SignoutView.as_view(), name="hr_logout"),
    path('index/', IndexView.as_view(), name="hr_home"),
    path('category/', CategoryCreateListView.as_view(), name="hr_category"),
    path('category/<int:pk>/delete/',CatDeleteView.as_view(), name="cat_delete"),
    path('add_jobs/', JobAddView.as_view(), name="add_job"),
    path('list_jobs/', JobListView.as_view(), name="list_job"),
    path('complete_jobs/', JobCompleteView.as_view(), name="complete_job"),
    path('update_jobs/<int:pk>/', JobUpdateView.as_view(), name="update_job"),
    path('job/delete/<int:pk>/', JobDeleteView.as_view(), name="delete_job"),
    path('applications/<int:pk>/', JobApplicationListView.as_view(), name="applications_job"),


]
