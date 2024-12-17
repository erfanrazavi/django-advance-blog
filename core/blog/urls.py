from django.urls import path
from .views import *
from django.views.generic import TemplateView , RedirectView

app_name = "blog"

urlpatterns = [
    path("cbv", IndexView.as_view(),name='cbv-i'),
    path("list-view/", PostList.as_view(),name='list-cbv'),        
    path("go-to-google", RedirectToGoogle.as_view(), name="redirect-google"),
]