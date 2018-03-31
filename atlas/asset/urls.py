from django.contrib import admin
from django.urls import path, include

from . import views as asset_views

urlpatterns = [
    path('', asset_views.index),
    path('add/', asset_views.add),
    path('scan/<uid>', asset_views.scan),
    path('<int:id>', asset_views.detail),
    path('hardware/', asset_views.hardware),
    path('software/', asset_views.software),
]
