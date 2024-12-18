from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

#getting user model object
# User = get_user_model()

class Post(models.Model):
    '''
    this is class to define posts for blog app

    '''
    author = models.ForeignKey('accounts.Profile' , on_delete=models.CASCADE)
    image = models.ImageField(null=True , blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('Category' , on_delete=models.SET_NULL , null=True)
    '''
    We put the category in a string because we wanted to define it after this class.
    If it wasn't in a string, the Category class would need to be defined before the Post class.
    ''' 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
