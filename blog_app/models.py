from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.

class PostMaster(models.Model):
    id=models.IntegerField(primary_key=True,null=False)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=500)
    pbl_date=models.DateField()
    image_url=models.CharField(max_length=200,null=True)

class UserPostMapper(models.Model):
    id=models.IntegerField(primary_key=True,null=False)
    post=models.ForeignKey(PostMaster,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

