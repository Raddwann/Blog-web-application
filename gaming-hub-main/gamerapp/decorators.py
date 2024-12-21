from functools import wraps
from django.http import HttpResponseForbidden

def require_login(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You must be logged in to access this page.")
        return view_func(request, *args, **kwargs)
<<<<<<< HEAD
    return wrapper
=======
    return wrapper
>>>>>>> 60fe71dd1ad27d0646fc72df5ce58c4da7f01dae
