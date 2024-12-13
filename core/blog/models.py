from django.db import models

# Create your models here.


class Post(models.Model):
    '''
    this is class to define posts for blog app

    '''
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    image = models.ImageField(null=True , blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    stauts = models.BooleanField()
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
    
