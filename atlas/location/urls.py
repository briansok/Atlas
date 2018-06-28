from django.urls import path

from . import views as location_views

urlpatterns = [
    path('', location_views.index, name='location-detail'),
    path('add/', location_views.add_location),
    path('<int:id>/edit/', location_views.edit_location),
    path('plan/', location_views.plan),
    path('plan/set/', location_views.set_plan_section),
    path('plan/get/', location_views.get_plan_section),
    path('plan/delete/', location_views.delete_plan_section),
    path('sections/', location_views.sections),
    path('sections/<int:id>', location_views.section_detail),
    path('sections/add/', location_views.add_section),
]
