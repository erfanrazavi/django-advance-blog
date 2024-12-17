from django.shortcuts import render , HttpResponse
from django.views.generic.base import TemplateView , RedirectView
from django.views.generic import ListView 
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
    

class PostList(ListView):
    '''
    a class based view (ListView) to show list of data into db
    
    '''
    # def get_queryset(self):
    #     posts = Post.objects.filter(status = True)
    #     return posts
    # queryset = Post.objects.filter(status = True)

    model = Post
    context_object_name = 'posts'
    paginate_by =  1
    ordering = '-id'
    
class RedirectToGoogle(RedirectView):
    url = 'https://google.com'
    

    
