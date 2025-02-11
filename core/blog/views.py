from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.utils import timezone
from .forms import PostForm
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# Create your views here.
class IndexView(TemplateView):
    """
    a class based view to show index page
    """

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "erf"
        context["posts"] = Post.objects.all()
        return context


class PostList(ListView):
    queryset = Post.objects.all()
    context_object_name = "posts"
    ordering = "-id"
    # paginate_by = 2 




class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


# def get_context_data(self, **kwargs):
# posts = super().get_context_data(**kwargs)
# posts['title'] = Post.objects.filter(status = 1)
# return posts
# class RedirectToGoogle(RedirectView):
# url = 'https://google.com'
"""
class PostCreateView(FormView):
    template_name = "contact.html"
    form_class = PostForm
    success_url = "/blog/post"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    # fields = ( 'title' , 'content' , 'status' , 'category',)
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = "/blog/post"


# API
# @api_view()
# def hello_world(request):
# return Response({'message' : 'Hello World'})


class PostListApiView(TemplateView):
    template_name = 'blog/post_list_api.html'
