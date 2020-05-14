from django.urls import path

from shop import views
# from shop.views import OutletList, OutletDetail
urlpatterns = [
    # path('create_customer/', views.create_customer, name='create_customer'),
    # path('<int:pk>/update_customer/', views.update_outlet, name='update_outlet'),
    # path('<int:pk>/delete_customer', views.delete_outlet, name='delete_outlet'),
    # path('', OutletList.as_view(), name='index_outlets'),
    # path('<int:pk>', OutletDetail.as_view(), name='show_outlet'),
    path('<int:pk>/create_order/', views.create_order, name='create_order')
]
