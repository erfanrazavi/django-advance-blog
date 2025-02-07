from django.test import TestCase

from accounts.models.users import User 
from accounts.models.profiles import Profile 
from ..models import Post

class TestPostModel(TestCase):
    # This method is executed before each test method to set up necessary test data
    def setUp(self):
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

    # Test to ensure that a Post is created successfully with valid data
    def test_create_post_with_valid_data(self):
        # Create a Post object with the profile as the author and other necessary details
        post = Post.objects.create(
            author = self.profile,  # Assign the profile as the author of the post
            title = 'test_title',   # Set the post title
            content = 'test_content',  # Set the post content
            status = True,           # Mark the post as active
            category = None         # Leave the category as None
        )

        # Check if the post exists in the database
        self.assertTrue(Post.objects.filter(pk=post.id).exists(),)

        # Assert that the title of the post is as expected
        self.assertEqual(post.title, 'test_title')