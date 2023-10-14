from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

class Data(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.CharField(max_length=1000)
    website=models.TextField()
    username=models.CharField(max_length=500,blank=True, null=True)
    password=models.TextField()
