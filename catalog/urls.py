from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('contacts/', views.contacts, name='contacts'),  # Страница контактов
]

# Обработка медиафайлов и статических файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

