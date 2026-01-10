from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('services/', views.service, name='services'),
    path('doctors/', views.doctors, name='doctors'),
]