from django.test import TestCase

from ..forms import PostForm
from ..models import Post, Category


class TestPostForms(TestCase):
    # Test case to check if the form is valid when provided with correct data
    def test_post_form_with_valid_data(self):
        # Create a category instance to use as a valid ForeignKey
        category = Category.objects.create(name='test_cat')

        # Initialize the form with valid data
        form = PostForm(data={
            'title': 'test_title',
            'content': 'test_content',
            'status': True,
            'category': category  # This should be category.id instead
        })

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    # Test case to check if the form is invalid when no data is provided
    def test_post_form_with_no_data(self):
        # Initialize the form without any data
        form = PostForm(data={})

        # The form should be invalid because required fields are missing
        self.assertFalse(form.is_valid())