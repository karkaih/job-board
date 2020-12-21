from django.shortcuts import render
from .models import  Info
from django.core.mail import send_mail
from project import settings
# Create your views here.

def send_message(request):
    myinfo = Info.objects.first()
    
    if request.method=='POST':
        subject = request.POST['subject']
        email =request.POST['email']
        message=request.POST['message']
        name = request.POST['name']
        send_mail( 
            'my name is ' + name +' subject is :==> '+ subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],     
        )



    return render(request,'contact/contact.html',{'myinfo':myinfo})