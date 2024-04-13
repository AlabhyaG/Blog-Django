from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    Gen_Choice=[
        ('M','Male'),
        ('F','Female'),
        ('O','other')
    ]
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=1,choices=Gen_Choice)
    

    def __str__(self):
        return self.user.username
  


    
