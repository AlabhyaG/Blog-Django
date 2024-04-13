from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    title_tag=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    date_created=models.DateTimeField(auto_now_add=True)
    body=models.TextField(blank=False,null=False)

    def __str__(self):
        return self.title + ', By-'+ str(self.author)