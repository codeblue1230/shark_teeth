from django.shortcuts import render
from .models import Post

def home(response):
    return render(response, "main/home.html", {})

def forums(resposne):
    all_posts = Post.objects.all()
    for p in all_posts:
        print(p.title)
        print(p.text)
    return render(resposne, "main/forums.html", {})
