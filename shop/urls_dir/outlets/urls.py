from django.urls import path

from shop import views
from shop.views import OutletList, OutletDetail
urlpatterns = [
    path('create_outlet/', views.create_outlet, name='create_outlet'),
    path('<int:pk>/update_outlet/', views.update_outlet, name='update_outlet'),
    path('<int:pk>/delete_outlet', views.delete_outlet, name='delete_outlet'),
    path('', OutletList.as_view(), name='index_outlets'),
    path('<int:pk>', OutletDetail.as_view(), name='show_outlet'),
    path('<int:pk>/create_product/', views.create_product, name='create_product')
]
