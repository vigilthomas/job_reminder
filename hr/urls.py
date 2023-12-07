from django.urls import path

from hr.views import *

urlpatterns = [
    path('', SigninView.as_view(), name="hr_login"),
    path('hr/logout', SignoutView.as_view(), name="hr_logout"),
    path('hr/index', IndexView.as_view(), name="hr_home"),
    path('hr/category', CategoryCreateListView.as_view(), name="hr_category"),
    path('hr/<int:pk>/delete', CatDeleteView.as_view(), name="cat_delete"),
    path('hr/add_jobs', JobAddView.as_view(), name="add_job"),
    path('hr/list_jobs', JobListView.as_view(), name="list_job"),
]
