# dating_platform/urls.py
from django.contrib import admin
from django.urls import path, include  # Убедитесь, что вы импортируете include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Включайте ваши маршруты API
]