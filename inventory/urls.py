from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('nuevo/', views.product_create, name='product_create'),
]