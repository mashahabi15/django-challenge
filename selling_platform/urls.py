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
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from selling_platform.security.superuser_permission import IsSuperuser

schema_view = get_schema_view(
   openapi.Info(
      title="Selling Platform APIs",
      default_version='v1',
      description="This is a Documentation on Selling Platform APIs",
      contact=openapi.Contact(email="ma.shahabi15@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[IsSuperuser],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Authentication URLs
    path('api/v1/selling_platform/jwt/create/', TokenObtainPairView.as_view(), name='jwt_token_create'),
    path('api/v1/selling_platform/jwt/refresh/', TokenRefreshView.as_view(), name='jwt_token_refresh'),

    # Users app URLs
    path('api/v1/selling_platform/users/', include(('users.urls', 'users'), namespace='v1_users')),

    # Stadiums app URLs
    path('api/v1/selling_platform/stadiums/', include(('stadiums.urls', 'users'), namespace='v1_stadiums')),

    # Matches app URLs
    path('api/v1/selling_platform/matches/', include(('matches.urls', 'users'), namespace='v1_matches')),

    # Reservations app URLs
    path('api/v1/selling_platform/reservations/', include(('reservations.urls', 'users'), namespace='v1_reservations')),

]
