from django.contrib import admin
from django.urls import path, include

from . import views as asset_views

urlpatterns = [
    path('', asset_views.index, name="assets"),
    path('hardware/', asset_views.hardware, name="hardware"),
    path('software/', asset_views.software, name="software"),
]
