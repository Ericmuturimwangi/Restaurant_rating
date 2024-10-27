from django.shortcuts import render
from ratings.models import Rating, Restaurant
from ratings.serializers import RatingSerializer, RestaurantSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    # permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


