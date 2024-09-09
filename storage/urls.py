from django.urls import path
from . import views

app_name = "storage"

urlpatterns = [
    path("fridge/text/", views.fridge_by_text, name="fridge_text"),
    path("fridge/image/", views.fridge_by_image, name="fridge_image"),
    path("fridge/stream/", views.fridge_stream, name="fridge_stream"),
    path("fridge/stream/response/", views.stream_response, name="stream_response"),
]
