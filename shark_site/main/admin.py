from django.contrib import admin
from .models import Post, Forum, Reply

admin.site.register(Post)
admin.site.register(Forum)
admin.site.register(Reply)