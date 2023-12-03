from rest_framework import routers, serializers, viewsets
from .models import Post



# Serializers define the API representation.


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = '__all__'