from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, RatingViewSet, UserProfileDetailView, TestAuthView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.authtoken import views 

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-auth/', views.obtain_auth_token),
    path('user/profile/', UserProfileDetailView.as_view(), name='user_profile'),
    path('api/test-auth/', TestAuthView.as_view(), name='test-auth'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'), #verifying the token

]