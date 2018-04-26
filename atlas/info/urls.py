from django.urls import path

from . import views as info_views

urlpatterns = [
    path('', info_views.index),
    path('updates/add/', info_views.add),
]
