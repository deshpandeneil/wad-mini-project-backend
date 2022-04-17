from wsgiref.validate import validator
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

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