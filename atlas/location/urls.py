from django.urls import path

from . import views as location_views

urlpatterns = [
    path('', location_views.index, name='location-detail'),
    path('add/', location_views.addLocation),
    path('<int:id>/edit/', location_views.editLocation),
    path('plan/', location_views.plan),
    path('plan/set/', location_views.setPlanSection),
    path('sections/', location_views.sections),
    path('sections/<int:id>', location_views.sectionDetail),
    path('sections/add/', location_views.addSection),
]
