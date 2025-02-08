from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name="get_abs_url")
    category = serializers.SlugRelatedField(
        many=False, slug_field="name", queryset=Category.objects.all()
    )
    # category = CategorySerializer()

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "image",
            "content",
            "category",
            "absolute_url",
            "snippet",
            "status",
            "relative_url",
            "created_date",
            "published_date",
        ]
        read_only_fields = ["author"]

    def get_abs_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context["kwargs"].get("pk"):
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("content", None)
        rep["category"] = CategorySerializer(
            instance.category, context={"request": request}
        ).data  # When we want to call the serializer elsewhere,
        # we pass the request along with it

        return rep

    def create(self, validated_data):

        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )

        return super().create(validated_data)
        # This method ensures that the 'author' field is automatically set
        # based on the currently logged-in user. It simplifies the process for
        # the client by not requiring the 'author' field in the request data,
        # as it is derived directly from the authenticated user's profile.
