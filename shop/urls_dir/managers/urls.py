from django.urls import path

from shop import views
from shop.views import ManagerList
urlpatterns = [
    path('<int:pk>/update_manager/', views.update_manager, name='update_manager'),
    path('<int:pk>/delete_manager', views.delete_manager, name='delete_manager'),
    path('', ManagerList.as_view(), name='index_managers')
]
