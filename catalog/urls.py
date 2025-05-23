from django.urls import path
from catalog.views import HomeView, ContactsView, product_detail

app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]

