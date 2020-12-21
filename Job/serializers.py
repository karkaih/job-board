#get data from model --- > Json
from .models import Job
from rest_framework import serializers


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job 
        fields = '__all__'