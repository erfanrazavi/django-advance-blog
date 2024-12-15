from django.shortcuts import render , HttpResponse
from django.views.generic.base import TemplateView , RedirectView
from .models import Post
from django.shortcuts import get_object_or_404
# Create your views here.

class IndexView(TemplateView):
    '''
        a class based view to show index page
    '''
     
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'erf'
        context['posts'] = Post.objects.all()
        return context
    
class RedirectToGoogle(RedirectView):
    url = 'https://google.com'
    

    
