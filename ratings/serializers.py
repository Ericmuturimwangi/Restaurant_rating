from rest_framework import serializers
from .models import Rating, Restaurant

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'score', 'restaurant']

    def create(self, validated_data):
        # assign the authenticated user to the user field
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class RestaurantSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'location', 'ratings']

