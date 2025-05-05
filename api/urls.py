from django.urls import path, include
from rest_framework_nested import routers
from order.views import CartItemViewSet, CartViewSet, HasOrderProduct, OrderViewSet, initiate_payment, payment_cancel, payment_fail, payment_success
from product.views import ProductImageViewSet, ProductViewSet, CategoryViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register("products", ProductViewSet, basename="products")
router.register("category", CategoryViewSet, basename="category")
router.register("carts", CartViewSet, basename="carts")
router.register("orders", OrderViewSet, basename="orders")

product_router = routers.NestedDefaultRouter(router, "products", lookup="product")
product_router.register('images', ProductImageViewSet, basename='product-images')
product_router.register('review', ReviewViewSet, basename='product-review')


cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-item')


urlpatterns = [
    
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls)),
    path('payment/', initiate_payment, name='payment'),
    path('payment/success/', payment_success, name='payment_success'),
    path('payment/fail/', payment_fail, name='payment_fail'),
    path('payment/cancel/', payment_cancel, name='payment_cancel'),
    path('has_order/<int:product_id>/', HasOrderProduct.as_view()),

]

