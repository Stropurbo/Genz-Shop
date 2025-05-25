from rest_framework import serializers
from blog.models import BlogModel

class BlogSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = BlogModel
        fields = ['id', 'name', 'description', 'image', 'created_at', 'updated_at']

