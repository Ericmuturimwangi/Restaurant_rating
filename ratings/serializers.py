from rest_framework import serializers
from .models import Rating, Restaurant

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'restaurant', 'user', 'rating', 'review']

class RestaurantSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'description', 'location', 'average_rating', 'ratings']
