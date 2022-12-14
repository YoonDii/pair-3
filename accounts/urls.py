from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("index/", views.index, name="index"),
    path("<int:pk>/detail", views.detail, name="detail"),
    path("update/", views.update, name="update"),
    path("logout/", views.logout, name="logout"),
]
