from django.shortcuts import render
from ratings.models import Rating, Restaurant
from ratings.serializers import RatingSerializer, RestaurantSerializer, UserProfileSerializer
from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import UserProfile
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [AllowAny] 


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [AllowAny]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        try:
            return self.request.user.userprofile
        except UserProfile.DoesNotExist:
            raise NotFound("User profile does not exist")
    


class TestAuthView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message":"Authenticated successfully!"})