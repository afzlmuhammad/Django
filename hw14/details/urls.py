from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.product_create, name='product_create'),

    path('<int:pk>/detail/', views.product_detail, name='product_detail'),

    path('<int:pk>/pdf/', views.generate_pdf, name='generate_pdf'),

    path('send_product_email/<int:pk>/', views.send_product_email, name='send_product_email'),
]