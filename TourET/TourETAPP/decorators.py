from django.shortcuts import redirect
from django.http import HttpResponse

def visitor_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_visitor:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapped_view

def admin_user_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_admin:            
            return view_func(request, *args, **kwargs)
        else:
            #return redirect('admin')
            return HttpResponse('You are not authorized to access this content.')
    return wrapper_func