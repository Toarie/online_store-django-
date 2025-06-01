from django.urls import path
from .views import (
    home,
    contacts,
    ProductDetailView,
    product_list,
    product_create,
    product_update,
    product_delete
)

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/', product_list, name='product_list'),
    path('product/create/', product_create, name='product_create'),
    path('product/<int:pk>/update/', product_update, name='product_update'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),
]
