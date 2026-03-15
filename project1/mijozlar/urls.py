from django.urls import path
from .views import mijozlar_list

urlpatterns = [
    path('', mijozlar_list),
]
