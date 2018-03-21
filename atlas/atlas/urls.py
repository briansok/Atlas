from django.contrib import admin
from django.urls import path, include

from . import views as atlas_views

urlpatterns = [
    path('', atlas_views.index, name="index"),
    path('admin/', admin.site.urls),
]
