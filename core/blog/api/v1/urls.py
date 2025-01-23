from django.urls import path , include
from blog.api.v1.views import *

app_name = "api-view-v1"

urlpatterns = [
   path('post/' , PostList.as_view() , name='post-list' ),
   # path('post/<int:id>/' , postDetail , name='post-detail' ),
   path('post/<int:id>/' , PostDetail.as_view() , name='post-detail' ),

]   