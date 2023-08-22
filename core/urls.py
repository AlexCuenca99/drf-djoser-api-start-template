from django.urls import path
from django.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Base
    path("admin/", admin.site.urls),
    # Djoser
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/auth/", include("djoser.urls.social.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
