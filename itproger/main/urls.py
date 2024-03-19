from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('set/', views.setcookie),
    path('sho/', views.showcookie)
]
