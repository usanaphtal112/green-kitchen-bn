from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import (
    SignUpSerializer,
    LoginSerializer,
    UserSerializer,
    UserDetailsSerializer,
    LogoutSerializer,
    UserProfileSerializers,
)
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from .tokens import create_jwt_pair_for_user
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUnauthenticated, AdminOnlyPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model


# Create your views here.


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [IsUnauthenticated]

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
            return Response(
                data={"message": message, "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [IsUnauthenticated]

    @extend_schema(
        description="Login on your account",
        tags=["Users"],
        request=LoginSerializer,
    )
    def post(self, request: Request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        tokens = create_jwt_pair_for_user(user)
        response = Response(
            data={"message": "Login Successful", "tokens": tokens},
            status=status.HTTP_200_OK,
        )
        response.set_cookie(
            key="access_token",
            value=tokens["access"],
            httponly=True,  # Store the access token in cookies
        )
        response.set_cookie(
            key="refresh_token",
            value=tokens["refresh"],
            httponly=True,  # Store the refresh token in cookies
        )

        return response


class UserListView(APIView):
    permission_classes = [IsAuthenticated, AdminOnlyPermission]
    authentication_classes = [JWTAuthentication]
    User = get_user_model()

    @extend_schema(
        description="Login to your account",
        tags=["Users"],
        responses=UserSerializer,
    )
    def get(self, request):
        # Extract the access token from the cookies
        access_token = request.COOKIES.get("jwt_access_token")

        # Perform the JWT verification
        jwt_authentication = JWTAuthentication()
        try:
            user, _ = jwt_authentication.authenticate(request)
        except Exception as e:
            return Response(
                {"message": "Unauthenticated User"}, status=status.HTTP_401_UNAUTHORIZED
            )

        # Retrieve all users
        users = self.User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetailsView(APIView):
    User = get_user_model()
    permission_classes = [IsAuthenticated, AdminOnlyPermission]
    authentication_classes = [JWTAuthentication]

    @extend_schema(
        description="Retrieve user details based on user ID",
        tags=["Users"],
        responses={status.HTTP_200_OK: UserDetailsSerializer},
    )
    def get(self, request, user_id):
        try:
            user = self.User.objects.get(id=user_id)
        except self.User.DoesNotExist:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserDetailsSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return []

    @extend_schema(
        description="User logout",
        tags=["Users"],
        responses={status.HTTP_200_OK: None},
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response(
            {"message": "Logout successfully"}, status=status.HTTP_204_NO_CONTENT
        )

        # Delete tokens from cookies
        response = Response(
            {"message": "Logout successfully"}, status=status.HTTP_204_NO_CONTENT
        )
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

        return response


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        description="User profile",
        tags=["Users"],
        responses={status.HTTP_200_OK: UserProfileSerializers},
    )
    def get(self, request):
        user_profile = request.user
        serializer_class = UserProfileSerializers(user_profile)
        return Response(serializer_class.data)

    @extend_schema(
        description="Update user profile",
        tags=["Users"],
        responses={status.HTTP_200_OK: UserProfileSerializers},
        request=UserProfileSerializers,
    )
    def put(self, request):
        user_profile = request.user
        serializer_class = UserProfileSerializers(
            user_profile, data=request.data, partial=True
        )

        if serializer_class.is_valid():
            # Exclude the email field from updating
            serializer_class.validated_data.pop("email", None)

            if "address" not in serializer_class.validated_data:
                return Response(
                    {"address": ["Address field is mandatory."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            serializer_class.save()
            return Response(serializer_class.data)

        return Response(serializer_class.errors, status=400)
