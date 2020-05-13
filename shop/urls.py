from django.urls import path, include
from shop import views

urlpatterns = [
    path('', views.home, name='home'),
    path('outlets/', include('shop.urls_dir.outlets.urls')),
    path('tags/', include('shop.urls_dir.tags.urls')),
    path('vendors/', include('shop.urls_dir.vendors.urls')),
    path('managers/', include('shop.urls_dir.managers.urls')),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
