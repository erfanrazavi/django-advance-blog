from blog.api.v1.views import PostModelViewSet, CategoryModelViewSet
from rest_framework.routers import DefaultRouter


app_name = "api-view-v1"

router = DefaultRouter()

router.register("post", PostModelViewSet, basename="post")
router.register("category", CategoryModelViewSet, basename="category")

urlpatterns = router.urls

# urlpatterns = [
#    # path('post/' , PostList.as_view() , name='post-list' ),
#    # path('post/<int:id>/' , postDetail , name='post-detail' ),
#    # path('post/<int:id>/' , PostDetail.as_view() , name='post-detail' ),
#    path('post/' , PostViewSet.as_view({'get' : 'list' , 'post':'create'}) , name='post-list' ),
#    path('post/<int:pk>' , PostViewSet.as_view({'get' : 'retrieve' , 'put' : 'update' , 'patch' : 'partial_update' , 'delete':'destroy' }) , name='post-detail' ),
# ]
