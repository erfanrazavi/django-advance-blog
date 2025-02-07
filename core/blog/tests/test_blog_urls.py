from django.test import TestCase
from django.urls import reverse , resolve

from ..views import PostList, PostDetailView, PostCreateView, PostUpdateView

class TestUrl(TestCase):
    def test_blog_list_url_resolve(self):
        url = reverse('blog:list-cbv')
        self.assertEqual(resolve(url).func.view_class, PostList)
        
    def test_blog_detail_url_resolve(self):
        url = reverse('blog:post-detail' , kwargs={'pk' : 1})
        self.assertEqual(resolve(url).func.view_class, PostDetailView)
    
    def test_blog_create_url_resolve(self):
        url = reverse('blog:post-create')
        self.assertEqual(resolve(url).func.view_class, PostCreateView)
    
    def test_blog_update_url_resolve(self):
        url = reverse('blog:post-edit', kwargs={'pk' : 1})
        self.assertEqual(resolve(url).func.view_class, PostUpdateView)