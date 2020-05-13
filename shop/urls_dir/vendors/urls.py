from django.urls import path

from shop import views
from shop.views import VendorList, VendorDetail
urlpatterns = [
    path('create_vendor/', views.create_vendor, name='create_vendor'),
    path('<int:pk>/update_vendor/', views.update_vendor, name='update_vendor'),
    path('<int:pk>/delete_vendor', views.delete_vendor, name='delete_vendor'),
    path('', VendorList.as_view(), name='index_vendors'),
    path('<int:pk>', VendorDetail.as_view(), name='show_vendor')
]
