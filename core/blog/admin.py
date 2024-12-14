from django.contrib import admin
from .models import Category , Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['author' ,'title' ,'status','category' ,'created_date' ,'published_date'] 
    search_fields = (
        'content' ,
           'title' ,
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
