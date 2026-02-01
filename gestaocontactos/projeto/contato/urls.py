from django.urls import path, include
from contato import views

urlpatterns = [
    path('', views.home, name='home'),
]

