from . import views
from django.urls import path, include
from app_smart.api.viewssets import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.abre_index, name='abre_index'),
    path('api/create_user', CreateUserAPIViewSet.as_view(), name='create_user'),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]