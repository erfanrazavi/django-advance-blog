

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET' , 'POST'])
def postList(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status =True)
        serializer = PostSerializer(posts,many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()    
        return Response(serializer.data)
@api_view(["GET" , "PUT" , 'DELETE'])
def postDetail(request , id):
   post = get_object_or_404(Post,pk=id , status =True)
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
       return Response({'detail' : 'Item removed successfully'},status=status.HTTP_204_NO_CONTENT)   
                
   