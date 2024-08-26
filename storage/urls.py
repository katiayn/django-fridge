from django.urls import path
from . import views

app_name = "storage"

urlpatterns = [
    path("fridge/text/", views.fridge_by_text, name="fridge_text"),
    path("fridge/image/", views.fridge_by_image, name="fridge_image"),
]
