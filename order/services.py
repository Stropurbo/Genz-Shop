from order.models import Order, OrderItem, Cart
from django.db import transaction
from rest_framework.exceptions import PermissionDenied, ValidationError

class OrderServices:
    @staticmethod
    def create_order(user_id, cart_id):
        with transaction.atomic():
            try:
                cart = Cart.objects.select_related('user').get(pk=cart_id)
            except Cart.DoesNotExist:
                raise ValidationError("Cart not found.")  

            cart_items = cart.items.select_related('product').all()
            if not cart_items:
                raise ValidationError("Cart is empty.")  

            total_price = sum([item.product.price * item.quantity for item in cart_items])
            order = Order.objects.create(user_id=user_id, total_price=total_price)

            order_items = [
                OrderItem(  
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity,
                    total_price=item.product.price * item.quantity
                )
                for item in cart_items
            ]
            OrderItem.objects.bulk_create(order_items)  
            cart.delete()

            return order

    @staticmethod
    def cancel_order(order, user):
        if user.is_staff:
            order.status = Order.CANCELED
            order.save()
            return order
        if order.user != user:
            raise PermissionDenied("You can only cancel your own orders.")
        if order.status == Order.DELIVERED:
            raise ValidationError("You cannot cancel a delivered order.")
        order.status = Order.CANCELED
        order.save()
        return order
