"""
Django settings for e_commerce_api project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from environs import Env
from datetime import timedelta
import os

import cloudinary
import cloudinary.uploader

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)
# DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    # Local Apps
    "accounts.apps.AccountsConfig",
    "shops.apps.ShopsConfig",
    "cart.apps.CartConfig",
    "order.apps.OrderConfig",
    "payment.apps.PaymentConfig",
    "guest_user.apps.GuestUserConfig",
    # third party apps
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "drf_spectacular",
]

AUTH_USER_MODEL = "accounts.User"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "order.middleware.CartMiddleware",  # Custom Middleware
]

ROOT_URLCONF = "e_commerce_api.urls"

REST_FRAMEWORK = {
    "NON_FIELD_ERRORS_KEY": "errors",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        # "rest_framework.authentication.TokenAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    # "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=2),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "SIGNING_KEY": env.str("SECRET_KEY"),
    "AUTH_HEADER_TYPES": ("Bearer",),
    # "Bearer <Token>"
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "e_commerce_api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": env.str("DATABASE_NAME"),
#         "USER": env.str("DATABASE_USER"),
#         "PASSWORD": env.str("DATABASE_PASSWORD"),
#         "PORT": env.str("DATABASE_PORT"),
#         "HOST": env.str("DATABASE_HOST"),
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env.str("DATABASE_NAME"),
        "USER": env.str("DATABASE_USER"),
        "PASSWORD": env.str("DATABASE_PASSWORD"),
        "PORT": env.str("DATABASE_PORT"),
        "HOST": env.str("DATABASE_HOST"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_DIRS = []

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# Actual directory user files go to
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "mediafiles")

# URL used to access the media
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


SPECTACULAR_SETTINGS = {
    "TITLE": "E-COMMERCE API Project",
    "DESCRIPTION": "E-Commerce project using Django Rest Framework(DRF)",
    "VERSION": "1.0.0",
    # OTHER SETTINGS
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  # 7 days in seconds

CART_SESSION_ID = "cart"


CORS_ALLOWED_ORIGINS = [
    "https://naphtal112.pythonanywhere.com",
    "http://localhost:5173",
    "http://localhost:8000",
    "http://localhost:3000",
]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

SITE_URL = "http://localhost:3000/"
SITE_URL = "http://localhost:5173/"
API_URL = "http://localhost:8000/"


CSRF_TRUSTED_ORIGIN = [
    "https://naphtal112.pythonanywhere.com",
    "http://localhost:5173",
    "http://localhost:8000",
    "http://localhost:3000",
]


# Set up Cloudinary configuration
cloudinary.config(
    cloud_name=env.str("CLOUDINARY_NAME"),
    api_key=env.str("CLOUDINARY_API_KEY"),
    api_secret=env.str("CLOUDINARY_SECRET_KEY"),
)


# Stripe settings
STRIPE_PUBLISHABLE_KEY = env.str("STRIPE_PUBLISHABLE_KEY")  # Publishable key
STRIPE_SECRET_KEY = env.str("STRIPE_SECRET_KEY")  # Secret key
STRIPE_API_VERSION = "2022-11-15"
STRIPE_SECRET_WEBHOOK = env.str("STRIPE_SECRET_WEBHOOK")


# front-end URL's
CHECKOUT_SUCCESS_URL = "http://localhost:5173/checkout/success/"
CHECKOUT_FAILED_URL = "http://localhost:5173/checkout/failed/"
