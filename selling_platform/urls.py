"""selling_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Authentication URLs
    path('api/v1/selling_platform/jwt/create/', TokenObtainPairView.as_view(), name='jwt_token_create'),
    path('api/v1/selling_platform/jwt/refresh/', TokenRefreshView.as_view(), name='jwt_token_refresh'),

    # Users app URLs
    path('api/v1/selling_platform/users/', include(('users.urls', 'users'), namespace='v1_users')),

    # Stadiums app URLs
    path('api/v1/selling_platform/stadiums/', include(('stadiums.urls', 'users'), namespace='v1_stadiums')),

]
