from django.urls import path

from . import views as asset_views

urlpatterns = [
    path('', asset_views.index, name="asset-list"),
    path('scan/<uid>', asset_views.scan),
    path('<int:id>/edit', asset_views.edit),
    path('<int:id>/delete', asset_views.delete),

    path('hardware/', asset_views.hardware_list),
    path('hardware/<int:id>', asset_views.hardware_detail, name="hardware-detail"),

    path('software/', asset_views.software_list),
    path('software/<int:id>', asset_views.software_detail, name="software-detail"),
    path('software/<int:id>/add-license', asset_views.add_license),

    path('license/<int:id>/edit', asset_views.edit_license, name="edit-license"),
    path('license/<int:id>/delete', asset_views.delete_license, name="delete-license"),

    path('<str:asset>/add/', asset_views.add),
    path('request/', asset_views.request),
]
