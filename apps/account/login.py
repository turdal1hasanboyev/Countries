from django.views import View

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from django.contrib import messages


class LogInView(View):
    """
    View for handling user login.
    """

    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')
