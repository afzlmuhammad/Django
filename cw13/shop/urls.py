from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path('list/', views.list_products, name='list_products'),
    path('update/<int:pk>/', views.update_product, name='update_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
]