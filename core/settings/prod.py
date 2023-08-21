from .base import *


DEBUG = env("DEBUG")

ALLOWED_HOSTS = []


# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("DJANGO_RDS_DB_NAME"),
        "USER": env("DJANGO_RDS_USER"),
        "PASSWORD": env("DJANGO_RDS_PASSWORD"),
        "HOST": env("DJANGO_RDS_HOST"),
        "PORT": env("DJANGO_RDS_PORT"),
    }
}


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
DOMAIN = ""
SITE_NAME = "Base DRF-Djoser-API-Start-Template"
