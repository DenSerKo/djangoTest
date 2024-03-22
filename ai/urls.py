from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("story/", views.story, name="story"),
    path("questions/", views.questions, name="questions"),
]