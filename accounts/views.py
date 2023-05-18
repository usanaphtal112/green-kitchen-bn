from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import SignUpSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from .tokens import create_jwt_pair_for_user

# Create your views here.


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    @extend_schema(
        description="Create a new user account",
        tags=["Users"],  # Set the title here
    )
    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            message = "User account created successfully"
            return Response(data={"message": message}, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    description="Create a new user account",
    tags=["Users"],  # Set the title here
)
class LoginView(APIView):
    permission_classes = []

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = HttpResponse()
            response.set_cookie(
                key="jwt_access_token",
                value=tokens["access"],
                httponly=True,  # Store the access token in cookies
            )
            response.set_cookie(
                key="jwt_refresh_token",
                value=tokens["refresh"],
                httponly=True,  # Store the refresh token in cookies
            )
            response = {"message": "Login Successfull", "tokens": tokens}
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Invalid email or password"})
