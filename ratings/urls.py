from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns=[
    path('', include(router.urls)),
]