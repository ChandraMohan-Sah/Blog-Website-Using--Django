from django.urls import path

from .import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="all-posts-page"),
    path("post-detail/<slug:slug>", views.post_detail, name="post-detail-page") #/posts/my-first-post
]
