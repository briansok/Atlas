from django.urls import path

from . import views as asset_views

urlpatterns = [
    path('', asset_views.index, name="asset-list"),
    path('scan/<uid>', asset_views.scan),
    path('<int:id>/edit', asset_views.edit),
    path('<int:id>/delete', asset_views.delete),

    path('hardware/', asset_views.hardwareList),
    path('hardware/<int:id>', asset_views.hardwareDetail, name="hardware-detail"),

    path('software/', asset_views.softwareList),
    path('software/<int:id>', asset_views.softwareDetail, name="software-detail"),
    path('software/<int:id>/add-license', asset_views.addLicense),

    path('<str:asset>/add/', asset_views.add),
    path('request/', asset_views.request),
]
