from django.urls import path

from . import views as location_views

urlpatterns = [
    path('', location_views.index),
]
