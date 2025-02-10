from django.views import View

from django.shortcuts import redirect

from django.contrib.auth import logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch') # This decorator is used to check if the user is logged in or not
class LogOutView(View):
    """
    This view is used to log out the user from the system.
    """
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'You have been logged out successfully')
        return redirect('home')
    