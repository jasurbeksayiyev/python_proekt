from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('menu/', views.menu, name='menu'),
    path('registration_success/', views.registration_success, name='registration_success'),
]
