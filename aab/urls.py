from django import views
from django.urls import path
# from .views import home
from . import views

urlpatterns = [
    path('', views.home ),
]
