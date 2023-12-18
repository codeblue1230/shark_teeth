from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("forums/", views.forums, name="forums"),
    path("create/", views.create, name="create"),
    path("profile/", views.profile, name="profile"),
    path("shells/", views.shells, name="shells"),
    path("teeth/", views.teeth, name="teeth"),
    path("profile/<int:id>", views.any_profile, name="any_profile")
]