from django.urls import path

from . import views

app_name = "asks"

urlpatterns = [
    path("submit/", views.submit_form, name="submit_form"),
]
