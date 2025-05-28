from django.urls import path
from catalog.views import HomeView, ContactsView, product_detail

app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/', views.product_list, name='product_list'),
    path('product/create/', views.product_create, name='product_create'),
    path('product/<int:pk>/update/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
]

