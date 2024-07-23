from django.urls import path
from . import views

app_name = "storage"

urlpatterns = [
    path("fridge/", views.fridge, name="fridge"),
]