from django.urls import path

from . import views

app_name = "emails"

urlpatterns = [
    path("collect/", views.collect_email, name="collect_email"),
]
