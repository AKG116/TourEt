from django.urls import path
from . import views
from TourETAPP.urls import *

urlpatterns = [
    path('Tour_admin/', views.Tour_admin, name='Tour_admin'),
    path('logout/', views.logout, name='logout'),
    path('get_statistics/', views.get_statistics, name='get_statistics'),
]

