from main.jsonenv import env
import datetime

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # 'rest_framework.authentication.SessionAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}

REST_AUTH = {
   'JWT_AUTH_HTTPONLY':False,
   'USE_JWT': True,
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=60),
   'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
}