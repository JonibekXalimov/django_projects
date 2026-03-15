from django.urls import path
from .views import dorilar_list

urlpatterns = [
    path("",dorilar_list)
]
