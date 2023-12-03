from rest_framework import routers, serializers, viewsets
from .models import Post
from django.contrib.auth.models import User



# Serializers define the API representation.

class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = ['id','username','email']


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    category = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = '__all__'