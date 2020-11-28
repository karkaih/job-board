from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import Job
from .form import ApplyForm ,JobForm
from django.urls import reverse
# Create your views here.

def job_list(request) :
    job_list= Job.objects.all()

    paginator = Paginator(job_list, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'jobs' : page_obj }
    print(job_list)
    return render(request,'Job/job_list.html',context)


def job_detail(request,slug) :
    job_detail= Job.objects.get(slug=slug)

    if request.method=='POST':
        form =ApplyForm(request.POST,request.FILES)

        if form.is_valid():
            myform = form.save(commit=False)
            myform.job=job_detail
            myform.save()
            

    else :
        form = ApplyForm()

    context = {'jobs' : job_detail , 'form':form}
    print(job_list)
    return render(request,'Job/job_detail.html',context)



def add_job(request) :

    if request.method == 'POST':
        form =JobForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner=request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else :
        form = JobForm()


    
    return render(request,'Job/add_job.html',{'form':form})