from django.urls import path

from . import views as person_views

urlpatterns = [
    path('', person_views.index),
    path('<int:id>/', person_views.detail),
]
