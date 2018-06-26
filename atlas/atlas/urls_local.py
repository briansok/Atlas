from . import urls
from django.urls import path
from kirrassoconsumer.views import LoginView, LoginCompleteView

urls.urlpatterns += [
    path('login/', LoginView.as_view(), name='auth-login'),
    path('login-complete/', LoginCompleteView.as_view(), name='auth-login-complete'),
]
