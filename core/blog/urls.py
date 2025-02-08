from django.urls import path, include
from .views import (
    PostDeleteView,
    PostList,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    IndexView,
)

app_name = "blog"

urlpatterns = [
    path("cbv", IndexView.as_view(), name="cbv-i"),
    path("post/", PostList.as_view(), name="list-cbv"),
    #     # path("go-to-google", RedirectToGoogle.as_view(), name="redirect-google"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post-edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("api/v1/", include("blog.api.v1.urls")),
]
