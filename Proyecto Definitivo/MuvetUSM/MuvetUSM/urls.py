from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include
from apps.Core import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('registro/', views.registrar, name='registrar'),
    path('login/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.home, name='profile'),
]

