from django.urls import include,path
from .  import api
from . import views
app_name="Job"
urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('add',views.add_job,name='add_job'),
    path('<str:slug>',views.job_detail,name='jobdetail'),
    #api
    path('api/jobs',api.Job_List_api,name='Job_List_api'),
    path('api/jobs/<int:id>',api.job_detail_api,name='job_detail_api'),

    #class Based views
    path('api/v2/jobs',api.Job_List_Api.as_view(),name='Job_List_Api'),
    path('api/v2/jobs/<int:id>',api.JobDetail.as_view(),name='JobDetail'),

]
