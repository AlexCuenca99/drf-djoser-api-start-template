from .base import *

from datetime import timedelta


DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Database
if env("DEV_STAGE") == "initial":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "..", "db.sqlite3"),
        }
    }
elif env("DEV_STAGE") == "test":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": env("DJANGO_PSQL_DB_NAME"),
            "USER": env("DJANGO_PSQL_DB_USERNAME"),
            "PASSWORD": env("DJANGO_PSQL_DB_PASSWORD"),
            "HOST": env("DJANGO_PSQL_DB_HOST"),
            "PORT": env("DJANGO_PSQL_DB_PORT"),
        }
    }
else:
    raise Exception(
        "Dev stage is not configured properly. Please set initial, test or prod in .env DJANGO_DEV_STAGE."
    )


# Email
EMAIL_BACKEND = env("EMAIL_BACKEND")
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Guayaquil"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, "..", "static")
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
]


# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, "..", "media")
MEDIA_URL = "/media/"


# Domains
DOMAIN = "localhost:3000"
SITE_NAME = "Base DRF-Djoser-API-Start-Template"


# Cors headers
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
CORS_ALLOW_CREDENTIALS = True


# SimpleJWT
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}
