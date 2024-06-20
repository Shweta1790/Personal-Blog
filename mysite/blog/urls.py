from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("posts", views.viewAllPosts, name="view-all-post"),
    path("posts/<slug:slug>", views.viewPostDetail, name="post-detail-page"),
]
