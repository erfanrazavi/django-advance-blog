from rest_framework import serializers
from ...models import Post
class PostSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # content = serializers.CharField(max_length=255)
    
    class Meta:
        model = Post
        fields = ['id' , 'author', 'title' , 'content' , 'status' , 'created_date' , 'published_date']
