from datetime import date, timedelta
import datetime
from django.forms import DateField
from django.shortcuts import render
from rest_framework.response import Response
from order.models import Item, Order
from order.serializers import OrderSerializer
from product.models import Product
from rest_framework import generics
from user.models import Cart

from rest_framework.permissions import IsAuthenticated

# Create your views here.

class Checkout(generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user=request.user)
        if len(cart) > 0:
            total_price = 0
            total_quantity = 0
            eta = datetime.datetime.now() + timedelta(days=7)
            print(eta)
            order = Order(user_fk=request.user, eta=eta)
            order.save()
            print("eta s: ", eta)
            for i in cart:
                total_quantity += i.quantity
                product = i.product
                total_price += product.price * i.quantity
                item = Item(product_fk = product, order_fk=order, price=product.price, quantity=i.quantity)
                item.save()
                i.delete()
            order.total_price = total_price
            order.total_quantity = total_quantity
            order.save()
            return Response({"message": "your order has been placed"})
        else:
            return Response({"message": "cart is empty"})
        pass
