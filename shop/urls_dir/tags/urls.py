from django.urls import path

from shop import views
from shop.views import TagList
urlpatterns = [
    path('create_tag/', views.create_tag, name='create_tag'),
    path('<int:pk>/update_tag/', views.update_tag, name='update_tag'),
    path('<int:pk>/delete_tag', views.delete_tag, name='delete_tag'),
    path('', TagList.as_view(), name='index_tags'),
]
