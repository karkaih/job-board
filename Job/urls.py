from django.urls import include,path

from . import views
app_name="Job"
urlpatterns = [
    path('',views.job_list),
    path('<int:id>',views.job_detail,name='jobdetail'),
]
