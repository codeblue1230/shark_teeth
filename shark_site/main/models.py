from django.db import models

class Forum(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    picture = models.ImageField(upload_to=('files/teeth_images'))
    