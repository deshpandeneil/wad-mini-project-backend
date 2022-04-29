from xml.dom import ValidationErr
from django.shortcuts import render
from django.contrib.auth.models import User
from product.models import Product
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from user.models import Cart
from .serializers import CartSerializer, UserSerializer

from rest_framework_simplejwt.views import TokenViewBase
from .serializers import TokenObtainSerializer, TokenRefreshSerializer

# Create your views here.


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class UserCreate(generics.CreateAPIView):
    # authentication_classes = [authentication.TokenAuthentication]
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class UserDetail(generics.RetrieveAPIView):
    # authentication_classes = [authentication.TokenAuthentication]
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()


class CartList(generics.GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user=request.user)
        return Response(CartSerializer(cart, many=True).data)


class CartAdd(mixins.CreateModelMixin, generics.GenericAPIView):
    # authentication_classes = [authentication.TokenAuthentication]
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()

    
    def post(self, request, *args, **kwargs):
        print("HERE")
        print("args: ", args)
        print("kwargs: ", kwargs)
        data = {}
        user = request.user
        # data['product_pk'] = kwargs['pk']
        # data['quantity'] = request.data['quantity']
        print(data)
        product = Product.objects.get(id=kwargs['pk'])
        cart=Cart.objects.filter(user=user,product=product)

        if len(cart)>0:
            cart[0].quantity+=1
            cart[0].save()
            return Response(CartSerializer(cart[0]).data)
        else:
            cart_entry=Cart.objects.create(user=user,product=product,quantity=1)
            return Response(CartSerializer(cart_entry).data)

class CartRemove(generics.GenericAPIView):
    # authentication_classes = [authentication.TokenAuthentication]
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()

    
    def post(self, request, *args, **kwargs):
        print("HERE")
        print("args: ", args)
        print("kwargs: ", kwargs)
        data = {}
        user = request.user
        # data['product_pk'] = kwargs['pk']
        # data['quantity'] = request.data['quantity']
        print(data)
        product = Product.objects.get(id=kwargs['pk'])
        cart=Cart.objects.filter(user=user,product=product)
        if cart:
            print("cart is:", cart)
            print("cart[0] is:", cart[0])
            cart[0].quantity-=1
            if cart[0].quantity == 0:
                print("quantity is 0")
                cart[0].delete()
                return Response({})
            cart[0].save()
            return Response(CartSerializer(cart[0]).data)
        return Response({})

class CartDelete(ModelViewSet):

    def destroy(self, request, *args, **kwargs):
        if 'product_pk' not in request.data:
            raise ValidationErr({"product_pk": "This field is required"})
        Cart.objects.delete(id=request.data['product_pk'])
        return super(CartDelete, self).destroy(request, *args, **kwargs)


class TokenObtainPairView(TokenViewBase):
    """
        Return JWT tokens (access and refresh) for specific user based on username and password.
    """
    serializer_class = TokenObtainSerializer


class TokenRefreshView(TokenViewBase):
    """
        Renew tokens (access and refresh) with new expire time based on specific user's access token.
    """
    serializer_class = TokenRefreshSerializer
