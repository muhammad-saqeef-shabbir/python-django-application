from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('', views.say_hello)
]