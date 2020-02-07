from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from users.serializers import LoginUserSerializer, UserSerializer, CreateUserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from users.models import CustomUser
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "user": UserSerializer(
                user, context=self.get_serializer_context()).data,
            "token": token.key
        })


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.AllowAny]
    # parser_classes = [MultiPartParser, FormParser]

    def get_object():
        return self.request.user

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(
                user, context=self.get_serializer_context()).data,
            "token": token.key
        })


class Logout(APIView):
    def post(self, request, format=None):

        Token.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
