from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import RegisterForm

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Get the unsaved user instance
            user.date_joined = timezone.now()  # Set the date_joined field of the user
            user.save()  # Save the user instance with the updated date_joined
        return redirect("/")

    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})
