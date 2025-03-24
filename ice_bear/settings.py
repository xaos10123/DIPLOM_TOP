"""
Django settings for ice_bear project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG') == 'True'

ALLOWED_HOSTS = []



INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "dashboards",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "channels",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "django_q",
    "colorfield",
    "main",
    "goods",
    "users",
    "carts",
    "orders",
    "promotions",
    "delivery_panel",
]

JAZZMIN_SETTINGS = {
    "site_title": "Админка IBM",
    "site_header": "Админка IBM",
    "site_brand": "ICE BEAR MARKET",
    "welcome_sign": "Добро пожаловать в админ-панель!",
    "copyright": "ICE BEAR MARKET",
    "search_model":[ "goods.Product"],
    "site_logo": "img/logo_bear.svg",
    "user_avatar": None,
     "topmenu_links": [
        {"name": "Главная страница",  "url": "admin:index"},
        {"name": "Статистика", "url": "dashboards:dashboard", "icon": "fa-regular fa-chart-bar"},
        {"name": "Поступление на склад", "url": "goods:add_to_store", "icon": "fa-regular fa-chart-bar"},
        {"app": "goods"},
        {"app": "promotions"},
    ],
    "hide_apps": ["django_q"],
    "hide_models": ["orders.OrderItem", "users.Adress"],
    "navigation_expanded": False,
    "order_with_respect_to": ["auth", "goods", "goods.Product", "goods.Categories", "promotions", "carts"],
    "icons": {
        "goods": "fa-solid fa-boxes-stacked",
        "goods.Product": "fa-brands fa-product-hunt",
        "goods.Categories": "fa-solid fa-layer-group",
        "promotions": "fa-solid fa-percent",
        "promotions.Promo": "fa-solid fa-percent",
        "carts": "fa-solid fa-cart-shopping",
        "carts.Cart": "fa-solid fa-cart-plus",
        "orders": "fa-regular fa-folder",
        "orders.Order": "fa-solid fa-bag-shopping",
        "users": "fa-solid fa-users",
        "users.User": "fa-solid fa-user",
    },
    "custom_links": {
        None: [{
            "name": "Статистика", 
            "url": "dashboards:dashboard", 
            "icon": "fa-regular fa-chart-bar",
        }]
    },
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-primary",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}


MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ice_bear.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "ice_bear.wsgi.application"
ASGI_APPLICATION = "ice_bear.asgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "icebear",
        "USER": "admin",
        "PASSWORD": "101230",
        "HOST": "localhost",
        "PORT": "5433",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE')

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     BASE_DIR / 'static',
#     os.path.join(BASE_DIR, "static"),
# ]
# STATIC_ROOT = BASE_DIR / 'staticfiles'

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/user/login/"

Q_CLUSTER = {
    "name": "DjangORM",
    "workers": 4,
    "timeout": 90,
    "retry": 120,
    "queue_limit": 50,
    "bulk": 10,
    "orm": "default",
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}
