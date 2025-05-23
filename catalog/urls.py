from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.views import HomeView, ContactsView  # Импортируем CBV

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Используем as_view()
    path('contacts/', ContactsView.as_view(), name='contacts'),
]

# Обработка медиафайлов и статических файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

