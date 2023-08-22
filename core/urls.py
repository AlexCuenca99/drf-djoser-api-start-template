from django.urls import path
from django.urls import include
from django.contrib import admin

urlpatterns = [
    # Base
    path("admin/", admin.site.urls),
    # Djoser
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/auth/", include("djoser.urls.social.urls")),
]
