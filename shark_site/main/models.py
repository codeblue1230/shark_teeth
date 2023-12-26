from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Forum(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    picture = models.ImageField(upload_to=('files/teeth_images'))
    date_created = models.DateField(default=timezone.now)

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    f_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    date_created = models.DateField()
    
