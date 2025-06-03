from rest_framework import serializers
from posts.models import Post, Group, Comment, User


class GroupSerializer(serializers.ModelSerializer):
    """Group serializer class."""

    id = serializers.PrimaryKeyRelatedField(read_only=True, required=False)
    # description = serializers.CharField(required=False)

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    """Post serializer class."""

    id = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
    group = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Group.objects.all(),
        required=False
    )
    image = serializers.ImageField(required=False)
    pub_date = serializers.DateTimeField(read_only=True, required=False)

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date', 'group', )
        model = Post

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post


class CommentSerializer(serializers.ModelSerializer):
    """Comment serializer class."""

    # post = serializers.RelatedField()
    # # PostSerializer(required=True)
    # id = serializers.PrimaryKeyRelatedField(read_only=True)
    # author = serializers.SlugRelatedField(
    # slug_field='username', queryset=User.objects.all())
    # class Meta:
    #     model = Comment
    #     fields = ('id', 'text', 'author', 'post',)
    #
    # # def get_author(self, obj):
    # #     return obj.author.slug

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)
