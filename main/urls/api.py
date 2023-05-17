from django.urls import path, include

from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path(
        "v1/",
        include(
            [
                path('auth/', include('dj_rest_auth.urls')),
                path("",include("sales.urls")),
                path("", include(router.urls)),
            ]
        ),
    )
]
