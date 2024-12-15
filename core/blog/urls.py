from django.urls import path
from .views import indexView
from django.views.generic import TemplateView


urlpatterns = [
    path('fcb', indexView , name='FBV-test'),
    path("cbv", TemplateView.as_view(template_name="index.html")),

]