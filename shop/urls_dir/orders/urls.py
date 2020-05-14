from django.urls import path

from shop import views
from shop.views import OrderList, OrderDetail
urlpatterns = [
    path('<int:pk>', OrderDetail.as_view(), name='show_order'),
    path('<int:pk>/update_order/', views.update_order, name='update_order'),
    path('<int:pk>/delete_order', views.delete_order, name='delete_order'),
    path('', OrderList.as_view(), name='index_orders'),
]
