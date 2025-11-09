from django.contrib import admin
from django.urls import path
from catalog_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.search, name='search'),
    path('search-providers/', views.search, name='search_providers'),  ]
