from django.shortcuts import redirect
from django.http import HttpResponse

def unauthorised_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def can_add_song(allowed_users = []):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_users:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorised')
            return view_func(request, *args, **kwargs)
            
        return wrapper_func
    return decorator