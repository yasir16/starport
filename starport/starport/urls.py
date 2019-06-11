from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views as core_views

urlpatterns = [
    path("", core_views.home, name="home"),
    path("login", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("auth/", include("social_django.urls", namespace="social")),
    path("settings/", core_views.user_settings, name="user_settings"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("courses/", include("courses.urls")),
    path("admin/", admin.site.urls),
]
