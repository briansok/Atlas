from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views as atlas_views

""" Set login views based on your environment"""

urlpatterns = [
    path('', atlas_views.index, name="home"),
    path('assets/', include('asset.urls')),
    path('search/', atlas_views.search, name="search"),
    path('location/', include('location.urls')),
    path('users/', include('person.urls')),
    path('info/', include('info.urls')),
    path('admin/', admin.site.urls),

    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

try:
    from .urls_local import *
except ImportError:
    pass
