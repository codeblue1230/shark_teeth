from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

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
                p = Post(user=response.user, title=p_title, text=p_text, picture=p_img, forum=Forum.objects.get(id=1))
            elif p_choice == 2:
                p = Post(user=response.user, title=p_title, text=p_text, picture=p_img, forum=Forum.objects.get(id=2))

            p.save()

    else:
        form = CreateNewPost()

    return render(response, "main/create.html", {"form": form})


def forums(response):
    return render(response, "main/forums.html", {})


def teeth(response):
    t = Forum.objects.get(id=1) # Teeth Forum id=1
    s_posts = t.posts.all().order_by("-date_created", "-id") # posts is the name given to the Foreign Key connecting to the Forum Model (aka related_name)
    # s_posts gets posts from the teeth instance

    paginator = Paginator(s_posts, 5) # Show 5 posts per page
    page_number = response.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(response, "main/teeth.html", {"t": t, "page_obj": page_obj})


def shells(response):
    s = Forum.objects.get(id=2) # Shell Forum id=2
    shell_posts = s.posts.all().order_by("-date_created", "-id") # posts is the name given to the Foreign Key connecting to the Forum Model (aka related_name)
    # shell_posts gets posts from the shell instance

    paginator = Paginator(shell_posts, 5) # Show 5 posts per page
    page_number = response.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(response, "main/shells.html", {"s": s, "page_obj": page_obj})


# Logged in user's profile (aka view your own profile)
@login_required(login_url="/")
def profile(response):
    current_user = response.user
    user_posts = Post.objects.filter(user=current_user.id).order_by("-date_created", "-id")
    """
    user_posts is equal to the query below:
    SELECT * 
    FROM myApp_post
    WHERE user_id = <logged_in_user>
    ORDER BY date_created DESC, id DESC;
    """

    paginator = Paginator(user_posts, 5) # Turn above query into pages with 5 posts per page
    page_number = response.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(response, "main/profile.html", {"current_user": current_user, "page_obj": page_obj})

# View another user's profile
def any_profile(response, id):
    any_user = User.objects.get(id=id)
    if response.user.is_authenticated and response.user.id == any_user.id:
        return redirect("profile")
    """
    If the logged in user matches the id argument we can route the user back to their own profile page (if statement above),
    otherwise we route the user to a different user's profile page with the code below
    """
    user_posts = Post.objects.filter(user=any_user.id).order_by("-date_created", "-id")

    paginator = Paginator(user_posts, 5) # Turn above query into pages with 5 posts per page
    page_number = response.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(response, "main/any_profile.html", {"any_user": any_user, "page_obj": page_obj})

def a_post(response, id):
    p = Post.objects.get(id=id)
    return render(response, 'main/a_post.html', {"p": p})