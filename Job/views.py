from django.shortcuts import render

from .models import Job

# Create your views here.

def job_list(request) :
    job_list= Job.objects.all()
    context = {'jobs' : job_list}
    print(job_list)
    return render(request,'Job/job_list.html',context)

def job_detail(request,id) :
    job_detail= Job.objects.get(id=id)
    context = {'jobs' : job_detail}
    print(job_list)
    return render(request,'Job/job_detail.html',context)