from django.urls import path

from . import views as asset_views

urlpatterns = [
    path('', asset_views.index, name="asset-list"),
    path('scan/<uid>', asset_views.scan),
    path('<int:id>', asset_views.detail, name="asset-detail"),
    path('<int:id>/edit', asset_views.edit),
    path('<int:id>/delete', asset_views.delete),
    path('hardware/', asset_views.hardware),
    path('software/', asset_views.software),
    path('<str:asset>/add/', asset_views.add),
    path('request/', asset_views.request),
]
