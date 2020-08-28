from django.db import models
from django.contrib import auth
# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return self.username
class Cv(models.Model):
    person=models.ForeignKey(auth.models.User,on_delete=models.CASCADE)
    phone=models.PositiveIntegerField(blank=True,null=True)
    achievement=models.TextField()
    skills=models.TextField()
    highSchool=models.CharField(max_length=360)
    highSchoolPercetage=models.FloatField()
    collegeName=models.CharField(max_length=360)
    degree=models.CharField(max_length=360,default='B.tech')
    collegeGpa=models.FloatField()
    experiance=models.TextField(null=True,blank=True)
    projects=models.TextField(null=True,blank=True)
    CVname=models.CharField(max_length=200,default='MyCv',null=True,blank=True)
    def __str__(self):
        return self.person.username
