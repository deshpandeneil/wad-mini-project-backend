from dataclasses import field
from urllib import request
from product.models import Product

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cart, Profile

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

def required(value):
    if value is None:
        raise serializers.ValidationError('This field is required')

class UserSerializer(serializers.ModelSerializer):

    class ProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            exclude = ('user',)
    
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'profile']
    
    @staticmethod
    def create(validated_data):
        print(type(validated_data))

        if 'email' not in validated_data:
            raise serializers.ValidationError({"email": "This field is required"})

        if 'first_name' not in validated_data:
            raise serializers.ValidationError({"first_name": "This field is required"})

        if 'last_name' not in validated_data:
            raise serializers.ValidationError({"last_name": "This field is required"})

        if 'profile' in validated_data.keys():
            profile_data = validated_data.pop('profile')
            user_instance = User.objects.create_user(**validated_data)
            Profile.objects.create(user=user_instance, **profile_data)
        else:
            user_instance = User.objects.create_user(**validated_data)
            Profile.objects.create(user=user_instance)
        return user_instance


class CartSerializer(serializers.ModelSerializer):
        class Meta:
            model = Cart
            exclude = ('user', 'product', 'quantity')
            
        # def validate(self, data):
        #     """
        #     Check that the start is before the stop.
        #     """
        #     print('DATA IS: ', data.keys)
        #     if 'product_pk' in data:
        #         print(data)
        #         return data
        #     raise serializers.ValidationError({"product_pk": "This field is required"})
            

        @staticmethod
        def create(validated_data):
            if 'product_pk' not in validated_data:
                raise serializers.ValidationError({"product_pk": "This field is required"})
            user=request.user
            print("USER IS: ", user)
            product_pk=validated_data.pop('product_pk')
            product = Product.objects.get_object_or_404(id=product_pk)
            cart=Cart.objects.filter(user=user,product=product)

            if len(cart)>0:
                cart[0].quantity+=1
                cart[0].save()
                return cart[0]
            else:
                cart_entry=Cart.objects.create(user=user,product=product,quantity=1)
                return cart_entry


class TokenObtainSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
        }
        return data


class TokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
        }
        return data
