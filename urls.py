from django.contrib import admin
from django.urls import include, path

import views


urlpatterns = [
    path('', views.index, name='index'),
    path('oidc/', include('oidc_auth.urls')),
    path('admin/', admin.site.urls),
]
