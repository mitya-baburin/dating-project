# api/urls.py
from django.urls import path, include
#from .views import profile_list  # Убедитесь, что это правильный импорт
from api.views import profile_list as my_profile_list 

urlpatterns = [
    path('profiles/', my_profile_list, name='profile_list'),
    #path('profiles/', profile_list, name='profile_list'),  # Здесь должны быть ваши маршруты
]