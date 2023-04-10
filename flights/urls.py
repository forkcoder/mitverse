from django.urls import path
from . import views

app_name = "flights"
urlpatterns = [
    path("", views.index, name="name"),
    path("<int:flight_id>", views.flight, name="flight")
]
