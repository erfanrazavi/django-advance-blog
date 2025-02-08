from django.db import models
from django.urls import reverse


class Post(models.Model):
    """
    this is class to define posts for blog app

    """

    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    """
    We put the category in a string because
    we wanted to define it after this class.
    If it wasn't in a string, the Category
    class would need to be defined before the Post class.
    """
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.content[:3]

    def get_absolute_api_url(self):
        return reverse("blog:api-view-v1:post-detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
