from django.urls import path

from . import views as asset_views

urlpatterns = [
    path('', asset_views.index),
    path('scan/<uid>', asset_views.scan),
    path('<int:id>', asset_views.detail),
    path('<int:id>/edit', asset_views.edit),
    path('hardware/', asset_views.hardware),
    path('software/', asset_views.software),
    path('<str:asset>/add/', asset_views.add),
    path('request/', asset_views.request),
]
