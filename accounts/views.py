from django.shortcuts import render

from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import SignUpSerializer
from drf_spectacular.utils import extend_schema

# from rest_framework.views import APIView


# from .tokens import create_jwt_pair_for_user

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
            # response = {"message": "User Created Successfully", "data": serializer.data}
            # return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
