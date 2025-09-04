# api/urls.py
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api.views import profile_list as my_profile_list

from .views import dislike_profile, like_profile, view_profile

urlpatterns = [
    path("profiles/", my_profile_list, name="profile_list"),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profiles/like/", like_profile, name="like_profile"),
    path("profiles/dislike/", dislike_profile, name="dislike_profile"),
    path("profiles/view/", view_profile, name="view_profile"),
]
