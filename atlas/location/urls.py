from django.urls import path

from . import views as location_views

urlpatterns = [
    path('', location_views.index),
    path('<int:id>/edit/', location_views.editLocation),
    path('sections/', location_views.sections),
    path('sections/add/', location_views.add),
]
