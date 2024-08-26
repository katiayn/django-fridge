from django.urls import path
from . import views

app_name = "storage"

urlpatterns = [
    path("fridge/text/", views.fridge_by_text, name="fridge_text"),
]
