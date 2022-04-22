from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/Student/',null=True,blank=True)
    age = models.IntegerField(max_length=3,null=False,default=0)
   
    @property
    def get_name(self):
        return self.user.username
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name

    @property
    def get_age(self):
        return self.age