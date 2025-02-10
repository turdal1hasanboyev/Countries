from django.shortcuts import render, redirect

from django.views import View
from django.contrib import messages

from apps.base.models import SubEmail


class ProfileView(View):
    """
    View to display user's profile information.
    """

    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        sub_email = request.POST.get("sub_email")

        if sub_email:
            if SubEmail.objects.filter(email=sub_email).exists():
                messages.error(request, 'Email already exists')
            else:
                SubEmail.objects.create(email=sub_email)
                messages.success(request, 'Email added successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Please enter a valid email')
            return redirect('profile')
