from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import authenticate
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'email', 'age',
                  'joined_at', 'is_superuser')


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])

        if user:
            return user
        raise serializers.ValidationError(
            "Unable to log in with provided credentials.")


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'email', 'age', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data['email'],
            validated_data['password'],
            age=validated_data.get("age"),
            name=validated_data.get("name"),

        )

        return user


class CreateSuperUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'email', 'age', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_superuser(
            validated_data['email'],
            validated_data['password'],
            name=validated_data['name'],
            age=validated_data['age'],
        )
        return user
