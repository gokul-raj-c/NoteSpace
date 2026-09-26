from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    #date_posted=models.DateTimeField(auto_now_add=True)  #we cannot update it
    date_posted=models.DateTimeField(default=timezone.now) 
    author=models.ForeignKey(User,on_delete=models.CASCADE)  #if user deleted then post deleted

    def __str__(self):
        return self.title