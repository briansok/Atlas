from django.contrib import admin
from django.urls import path, include

from . import views as asset_views

urlpatterns = [
    path('', asset_views.index, name="assets"),
    path('add', asset_views.add, name="add"),
    path('<int:id>', asset_views.detail, name="asset"),
    path('hardware', asset_views.hardware, name="hardware"),
    path('software', asset_views.software, name="software"),
]
