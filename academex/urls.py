from django.urls import path

from academex import views

app_name = "academex"
urlpatterns = [
    path("", views.exchange, name="exchange")
]
