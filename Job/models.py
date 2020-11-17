from django.db import models

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
class Job(models.Model):#Table
    title = models.CharField(max_length=100)#colmun
    #location
    job_type = models.CharField(max_length=15,choices=Job_Type)    
    
    description = models.TextField(max_length=1000)
    publish = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    def __str__(self) :
        return self.title