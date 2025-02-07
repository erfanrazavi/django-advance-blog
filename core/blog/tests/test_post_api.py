from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime
import pytest

from accounts.models import User , Profile
from blog.models import Category

@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def common_user():
    user = User.objects.create_user(email='ali@ali.com',password='hasaniiii1234',is_verified=True)
    return user

@pytest.fixture
def common_category():
    category = Category.objects.create(name='erfan')
    return category

    






@pytest.mark.django_db
class TestPostApi:
    client = APIClient()    
    def test_get_post_response_200_status(self,api_client):
        
        url = reverse('blog:api-view-v1:post-list')
        response = api_client.get(url)
        assert response.status_code == 200 
        
    def test_create_post_response_401_status(self,api_client,common_category):
        url = reverse('blog:api-view-v1:post-list')
        data = {
            "title" : "test_title",
            "content" : "test_content",
            "status" : True,
            "category": common_category,
            "published_date" : datetime.now()
        }
        response = self.client.post(url, data)
        assert response.status_code == 401
    
    def test_create_post_response_201_status(self,api_client,common_user,common_category):
        url = reverse('blog:api-view-v1:post-list')
        data = {
            "title" : "test_title",
            "content" : "test_content",
            "status" : True,
            'category' : common_category,
            "published_date" : datetime.now()
        }
        # api_client.force_login(user=common_user)
        api_client.force_authenticate(user=common_user)
        response = api_client.post(url, data)
        print(response.data)
        assert response.status_code == 201
    
    def test_create_post_invalid_data_status(self,api_client,common_user,common_category):
        url = reverse('blog:api-view-v1:post-list')
        data = {
            "title" : "test_title",
            "content" : "test_content",
            "published_date" : datetime.now()
        }
        # api_client.force_login(user=common_user)
        api_client.force_authenticate(user=common_user)
        response = api_client.post(url, data)
        print(response.data)
        assert response.status_code == 400
