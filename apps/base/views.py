from django.shortcuts import render, redirect

from django.contrib import messages

from django.views import View

from ..base.models import SubEmail


class AboutView(View):
    """
    View for the about page.
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')
    
    def post(self, request, *args, **kwargs):
        sub_email = request.POST.get('sub_email')

        if SubEmail.objects.filter(email=sub_email).exists():
            messages.error(request, 'Email already subscribed')
            return redirect(request.META.get('HTTP_REFERER'))

        if sub_email:
            SubEmail.objects.create(email=sub_email)
            messages.success(request, 'Email subscribed')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Please enter your email address.')
            return redirect(request.META.get('HTTP_REFERER'))
