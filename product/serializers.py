from rest_framework import serializers
from product.models import Category, Product, Review, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']

class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer() 

    # category = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.all()
    # )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description','price','stock','category','created_at','updated_at', 'images']
    
    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError("Price must be greater than 0")
        return price
    
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()
    
    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'ratings', 'comment']
        read_only_fields = ['user', 'product']

    def get_user(self, obj):
        return {
            "id" : obj.user.id,
            "name" : obj.user.get_full_name()
        }
    
    def get_product(self, obj):
        return obj.product.name
    
    def create(self, validated_data):
        product_id = self.context['product_id']
        user = self.context['request'].user        
        return Review.objects.create(product_id=product_id, user=user, **validated_data)
