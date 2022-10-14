from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("index/",  views.index, name="index"),
    path("update/",  views.update, name="update"),
]
