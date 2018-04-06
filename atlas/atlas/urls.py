from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views as atlas_views

urlpatterns = [
    path('', atlas_views.index),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('assets/', include('asset.urls')),
    path('sections/', include('location.urls')),
    path('info/', include('info.urls')),
    path('admin/', admin.site.urls),
]
