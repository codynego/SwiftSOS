from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from . import views

urlpatterns = [
    path('api/token/', TokenObtainPairView, name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView, name='token_refresh'),
]
