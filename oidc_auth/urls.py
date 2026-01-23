from django.urls import path

from oidc_auth import views


urlpatterns = [
    path('login/', views.login_begin, name='oidc-login'),
    path('complete/', views.login_complete, name='oidc-complete'),
]
