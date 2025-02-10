from django.shortcuts import render, redirect

from django.views import View
from django.contrib import messages

from apps.base.models import SubEmail


class AboutView(View):
    """
    View for the about page.
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')

    def post(self, request, *args, **kwargs):
        url = request.META.get('HTTP_REFERER')
        sub_email = request.POST.get('sub_email')

        if sub_email:
            if SubEmail.objects.filter(email=sub_email).exists():
                messages.error(request, 'Email already exists')
            else:
                SubEmail.objects.create(email=sub_email)
                messages.success(request, 'Email added successfully')
            return redirect(url)
        else:
            messages.error(request, 'Email is required')
            return redirect(url)
