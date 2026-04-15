from django.urls import path
from producto.views import inicio

urlpatterns = [
    path('', inicio),
]



