from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Post, Forum
from .forms import CreateNewPost


def home(response):
    return render(response, "main/home.html", {})


@login_required(login_url="/")
def create(response):
    if response.method == "POST":
        form = CreateNewPost(response.POST, response.FILES) # When including a file you must also add response.FILES as an argument

        if form.is_valid():
            p_title, p_text = form.cleaned_data["title"], form.cleaned_data["text"]
            p_img, p_choice = form.cleaned_data["picture"], int(form.cleaned_data["s_or_t"][0])
            # Queryset comes out as a list so you must get the index and turn it to an integer
            print(p_choice)

            if p_choice == 1:
                p = Post(title=p_title, text=p_text, picture=p_img, forum=Forum.objects.get(id=1))
            elif p_choice == 2:
                p = Post(title=p_title, text=p_text, picture=p_img, forum=Forum.objects.get(id=2))

            p.save()

    else:
        form = CreateNewPost()

    return render(response, "main/create.html", {"form": form})


def forums(response):
    return render(response, "main/forums.html", {})


def teeth(response):
    t = Forum.objects.get(id=1) # In database the teeth forum has an id of 1
    s_posts = t.posts.all() # posts is the relate_name keyword argument from the Post Model Foreign Key
    # s_posts gets posts from the teeth instance

    return render(response, "main/teeth.html", {"t": t, "s_posts": s_posts})


def shells(response):
    s = Forum.objects.get(id=2) # In database the shell forum has an id of 2
    shell_posts = s.posts.all() # posts is the relate_name keyword argument from the Post Model Foreign Key
    # shell_posts gets posts from the teeth instance

    return render(response, "main/shells.html", {"s": s, "shell_posts": shell_posts})


@login_required(login_url="/")
def profile(response):
    current_user = response.user
    return render(response, "main/profile.html", {"current_user": current_user})