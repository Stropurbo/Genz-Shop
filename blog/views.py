from django.shortcuts import render
from rest_framework import viewsets
from blog.serializers import BlogSerializer
from blog.models import BlogModel
from product.permissions import IsAdminOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser

class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    permission_classes = [IsAdminOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        return BlogModel.objects.all()
    
