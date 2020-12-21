from django.urls import include,path
from .  import api
from . import views
app_name="Job"
urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('add',views.add_job,name='add_job'),
    path('<str:slug>',views.job_detail,name='jobdetail'),
    #api
    path('api/list',api.JobListapi,name='JobListapi'),
     
]
