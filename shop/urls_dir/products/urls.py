from django.urls import path

from shop import views
from shop.views import ProductList, ProductDetail
urlpatterns = [
    path('<int:pk>', ProductDetail.as_view(), name='show_product'),
    path('<int:pk>/update_product/', views.update_product, name='update_product'),
    path('<int:pk>/delete_product', views.delete_product, name='delete_product'),
    path('', ProductList.as_view(), name='index_products'),
]
