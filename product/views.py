from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.permission import IsAdminOrUser, IsAuthorOrReadonly
from product import serializers as productSz
from rest_framework.exceptions import PermissionDenied
from product.filters import ProductFilter
from product.models import Category, Product, ProductImage, Review
from django.db.models import Count


class ProductViewSet(ModelViewSet):
    serializer_class = productSz.ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['price']
    filterset_class = ProductFilter
    permission_classes = [IsAdminOrUser]

    def get_queryset(self):
        return Product.objects.prefetch_related("images").all()

class CategoryViewSet(ModelViewSet):
    serializer_class = productSz.CategorySerializer
    permission_classes = [IsAdminOrUser]

    def get_queryset(self):
        return Category.objects.annotate(product_count=Count("products")).all()
    
class ProductImageViewSet(ModelViewSet):
    serializer_class=productSz.ProductImageSerializer
    permission_classes = [IsAdminOrUser]

    def get_queryset(self):
        return ProductImage.objects.filter(product_id = self.kwargs.get('product_pk'))
    
    def perform_create(self, serializer):
        serializer.save(product_id = self.kwargs.get('product_pk'))

class ReviewViewSet(ModelViewSet):
    serializer_class = productSz.ReviewSerializer
    permission_classes = [IsAuthenticated and IsAuthorOrReadonly ]

    def perform_create(self, serializer):
        if not self.request.user or not self.request.user.is_authenticated:
            raise PermissionDenied("You have to login first.")
        serializer.save(user=self.request.user)
        
    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs.get('product_pk'))
    
    def get_serializer_context(self):
        return {'product_id': self.kwargs.get('product_pk')}



    