from xml.dom import ValidationErr
from product.models import Product, Category, Review, ProductImage
from product.serializers import ProductSerializers, CategorySerializer, ReviewSerializer,ProductImageSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from product.permissions import IsAdminOrReadOnly
from product.permissions import IsAuthorOrReadonly
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

class ProductViewset(ModelViewSet):
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price']
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Product.objects.prefetch_related('images').all()
    
    def perform_update(self, serializer):
        product = serializer.save()
        images = self.request.FILES.getlist('images')

        if images:        
            product.images.all().delete()
            for image in images:
                ProductImage.objects.create(product=product, image=image)


class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminOrReadOnly]
    def get_queryset(self):
        return ProductImage.objects.filter(product_id = self.kwargs.get('product_pk'))
    
    def perform_create(self, serializer):
        try:
            product = Product.objects.get(id=self.kwargs.get('product_pk'))
            serializer.save(product=product)
        except Product.DoesNotExist:
            raise ValidationErr("Product not found.")


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Category.objects.annotate(product_count=Count('products'))


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated and IsAuthorOrReadonly]

    def perform_create(self, serializer):
        if not self.request.user or not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged to post a review")
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs.get('product_pk'))

    def get_serializer_context(self):
        return {'product_id': self.kwargs.get('product_pk')}

