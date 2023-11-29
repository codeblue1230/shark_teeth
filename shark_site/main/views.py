from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import CreateNewPost

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewPost(response.POST, response.FILES) # When including a file you must also add response.FILES as an argument

        if form.is_valid():
            p_title, p_text = form.cleaned_data["title"], form.cleaned_data["text"]
            p_img = form.cleaned_data["picture"]
            
            p = Post(title=p_title, text=p_text, picture=p_img)
            p.save()

    else:
        form = CreateNewPost()

    return render(response, "main/create.html", {"form": form})

def forums(response):
    ls = Post.objects.all()
    return render(response, "main/forums.html", {"ls": ls})


    # all_posts = Post.objects.all()
    # for p in all_posts:
    #     print(p.title)
    #     print(p.text)

@login_required(login_url="/")
def profile(response):
    current_user = response.user
    return render(response, "main/profile.html", {"current_user": current_user})