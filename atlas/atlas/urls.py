from django.contrib import admin
from django.urls import path, include

from . import views as atlas_views

urlpatterns = [
    path('', atlas_views.index),
    path('assets/', include('asset.urls')),
    path('sections/', include('location.urls')),
    path('info/', include('info.urls')),
    path('admin/', admin.site.urls),
]
