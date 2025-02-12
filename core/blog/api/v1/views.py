from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .paginations import DefaultPagination
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from .permissions import IsOwnerOrReadOnly

"""@api_view(['GET' , 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postList(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status =True)
        serializer = PostSerializer(posts,many = True)
        # many for serializing a list or querysets
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data = request.data)
        # received data from http requests to server
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)"""
"""class PostList(APIView):
        permission_classes = [IsAuthenticatedOrReadOnly]
        serializer_class = PostSerializer
        '''getting a list of posts and creating new post'''
        def get(self , request):
            '''retrieving a list of post'''
            posts = Post.objects.filter(status =True)
            serializer = PostSerializer(posts,many = True)
            # many for serializing a list or querysets
            return Response(serializer.data)
        def post(self , request):
            '''creating a post with provided data'''
            serializer = PostSerializer(data = request.data)
            # received data from http requests to server
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)"""
"""class PostList(ListCreateAPIView):
    '''getting a list of posts and creating new post'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status =True)"""
"""@api_view(["GET" , "PUT" , 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request , id):
   post = get_object_or_404(Post,pk=id,status =True)
   if request.method == 'GET':
        serialize = PostSerializer(post)
        return Response(serialize.data)
   elif request.method == "PUT":
       serialize = PostSerializer(post , data=request.data)
       serialize.is_valid(raise_exception=True)
       serialize.save()
       return Response(serialize.data)
   elif request.method == 'DELETE':
       post.delete()
       return Response({'detail' : 'Item removed successfully'}
    ,status=status.HTTP_204_NO_CONTENT)"""
"""class PostDetail(APIView):
        ''' getting detail of the post and edit plus removing it'''
        permission_classes = [IsAuthenticatedOrReadOnly]
        serializer_class = PostSerializer
        def get(self , request , id):
            ''' retrieving the post data '''
            post = get_object_or_404(Post,pk=id,status =True)
            serialize = self.serializer_class(post)
            return Response(serialize.data)
        def put(self , request , id):
            ''' editing the post data '''
            post = get_object_or_404(Post,pk=id , status =True)
            serialize = self.serializer_class(post , data=request.data)
            serialize.is_valid(raise_exception=True)
            serialize.save()
            return Response(serialize.data)
        def delete(self , request , id):
            ''' deleting the post data '''
            post = get_object_or_404(Post,pk=id , status =True)
            post.delete()
            return Response({'detail' : 'Item removed successfully'},
            status=status.HTTP_204_NO_CONTENT)"""
"""class PostDetail(RetrieveUpdateDestroyAPIView):
    ''' getting detail of the post and edit plus removing it '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    lookup_field = 'id'
    queryset = Post.objects.filter(status =True)"""
"""class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    # lookup_field = 'id'
    queryset = Post.objects.filter(status =True)
    def list(self,request):
        serializer = self.serializer_class(self.queryset , many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)
    def create(self, request):
        pass
    def update(self, request, pk=None):
            post_object = get_object_or_404(Post,pk=pk , status =True)
            serialize = self.serializer_class(post_object , data=request.data)
            serialize.is_valid(raise_exception=True)
            serialize.save()
            return Response(serialize.data)
    def partial_update(self, request, pk=None):
        pass
    def destroy(self, request, pk=None):
        pass"""


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    # lookup_field='id'
    queryset = Post.objects.filter(status=True).order_by("-created_date")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "category": ["exact", "in"],
        "status": ["exact", "in"],
        "author": ["exact", "in"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ["-title", "id"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
