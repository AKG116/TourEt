from django.urls import path
from . import views
from TourDash.urls import *

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.visit_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('destinations/', views.destinations, name='destinations'),
    path('bookatour/', views.bookatour, name='bookatour'),
    path('create_package/', views.create_package, name='create_package'),
    path('profile/', views.create_destination, name='create_destination'),
    path('packages/', views.packages, name='packages'),
    path('update_profile/', views.update_profile, name='update_profile'),
]

