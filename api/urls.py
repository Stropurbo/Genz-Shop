from django.urls import path, include
from product.views import ProductViewset, CategoryViewSet, ReviewViewSet, ProductImageViewSet
from order.views import CartViewSet, CartItemViewSet, OrderViewSet
from rest_framework_nested import routers
from order.views import initiate_payment,payment_success,payment_cancel, payment_fail, HasOrderProduct
from blog.views import BlogViewSet
from getupdate.views import MailViewSet
from users.views import AdminUserViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewset, basename="products")
router.register('category', CategoryViewSet, basename="category")
router.register('carts', CartViewSet, basename="cart")
router.register('orders', OrderViewSet, basename="order")
router.register('blogs', BlogViewSet, basename="blog")
router.register('getupdate', MailViewSet, basename="getupdate")
router.register('admin/user', AdminUserViewSet, basename="adminuser")

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('review', ReviewViewSet, basename='product-review')
product_router.register('images', ProductImageViewSet, basename='product-images')

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename="cart-item")

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('payment/', initiate_payment, name='payment'),
    path('payment/success/', payment_success, name='payment_success'),
    path('payment/fail/', payment_fail, name='payment_fail'),
    path('payment/cancel/', payment_cancel, name='payment_cancel'),
    path('has_order/<int:product_id>/', HasOrderProduct.as_view()),    

]
