from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django_resized import ResizedImageField
# Create your models here.
'''
django  model field :
    -html widget
    -validation
    -db size
'''
Job_Type = (
('Full Time','Full Time'), 
('Part Time','Part Time'), 

)

def image_upload(instance,filename) :
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

class Job(models.Model):#Table
    owner =  models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)#colmun
    #location
    job_type = models.CharField(max_length=15,choices=Job_Type)     
    description = models.TextField(max_length=1000)
    publish = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    images  = models.ImageField(upload_to=image_upload)
    #images = ResizedImageField(size=[70, 200],quality=75, upload_to=image_upload)
    slug = models.SlugField(blank=True ,null=True)


    def save(self,*args,**kwargs) :
        self.slug = slugify(self.title)

        super(Job,self).save(*args,**kwargs)



    def __str__(self) :
        return self.title


class Category(models.Model) :
    name = models.CharField(max_length=25)

    def __str__(self) :
        return self.name




class Apply(models.Model):
    job = name = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website=models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    Created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    
