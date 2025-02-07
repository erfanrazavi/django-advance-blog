from django.test import TestCase , Client
from django.urls import reverse

from ..views import PostList , CreateView , DeleteView , UpdateView
from ..models import Post, Category
from accounts.models import Profile , User


class TestBlogView(TestCase):
    def setUp(self):
        self.client = Client()
         # Create a user to associate with the profile
        self.user = User.objects.create_user(email='n62@gmail.com',password='a/@1234567') 
        
        # Create a profile for the user or get the existing one (using get_or_create to avoid duplicates)
        self.profile, self.created = Profile.objects.get_or_create(
            user=self.user,  # Associate the profile with the user
            defaults={       # Set additional profile details
                'first_name': 'dfhaslk;dfjlkasdd',
                'last_name': 'lkaskdjflkasjdflk',
                'description': 'description'
            }
        )
        self.post = Post.objects.create(
            author = self.profile,  # Assign the profile as the author of the post
            title = 'test_title',   # Set the post title
            content = 'test_content',  # Set the post content
            status = True,           # Mark the post as active
            category = None         # Leave the category as None
        )
    
    def test_blog_index_url_response_successfully(self):
        url = reverse('blog:cbv-i')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(str(response.content).find('index'))
        self.assertTemplateUsed(response,template_name='index.html')

    def test_blog_post_detail_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse('blog:post-detail', kwargs={'pk' : self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_blog_post_detail_anonymous_response(self):
        url = reverse('blog:post-detail', kwargs={'pk' : self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

