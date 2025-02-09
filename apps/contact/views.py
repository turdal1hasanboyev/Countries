from django.shortcuts import render, redirect

from django.contrib import messages

from django.views import View

from .models import Contact
from apps.base.models import SubEmail


class ContactView(View):
    """
    View to handle contact form.
    """

    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        """
        Handle contact form submission.
        """

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        sub_email = request.POST.get('sub_email')

        url = request.build_absolute_uri()

        if SubEmail.objects.filter(email=sub_email).exists():
            messages.error(request, 'You are already subscribed to our newsletter.')
            # return redirect(url)
        
        if sub_email:
            SubEmail.objects.create(email=sub_email)
            messages.success(request, 'You have been successfully subscribed to our newsletter.')
            # return redirect(url)
        else:
            messages.error(request, 'Please enter your email address to subscribe to our newsletter.')
            # return redirect(url)

        if Contact.objects.filter(
            name=name,
            email=email,
            phone_number=phone_number,
            message=message,
        ).exists():
            messages.error(request, 'You have already sent a message.')
            return redirect(url)
        
        if name and email and phone_number and message:
            Contact.objects.create(
                name=name,
                email=email,
                phone_number=phone_number,
                message=message,
            )
            messages.success(request, 'Message sent successfully.')
            return redirect(url)
        else:
            messages.error(request, 'Please fill all fields.')
            return redirect(url)
