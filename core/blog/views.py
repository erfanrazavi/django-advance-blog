from django.shortcuts import render , HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def indexView(request):
    return render(request , 'index.html')