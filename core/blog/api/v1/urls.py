from django.urls import path , include
from blog.api.v1.views import *

app_name = "api-view-v1"

urlpatterns = [
   path('post/' , postList , name='post-list' ),
   path('post/<int:id>/' , postDetail , name='post-detai l' ),

]   