from django.shortcuts import render, redirect
from django.contrib.auth import logout as visitor_logout
from TourETAPP.views import *
from django.http import JsonResponse
from TourETAPP.models import *

def Tour_admin(request):
    total_num_users = CustomUser.objects.count()
    total_packages = Package.objects.count()
    total_destination = Destination.objects.count()
    context = {
        'total_num_users': total_num_users,
        'total_packages': total_packages,
        'total_destination': total_destination
    }
    return render(request, 'Tour_admin.html', context)


def get_statistics(request):
    total_num_users = CustomUser.objects.count()
    total_packages = Package.objects.count()
    total_destination = Destination.objects.count()

    data = {
        'total_num_users': total_num_users,
        'total_packages': total_packages,
        'total_destination': total_destination
    }

    return JsonResponse(data)

def logout(request):
    visitor_logout(request)
    return redirect('index')