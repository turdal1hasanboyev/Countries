from django.shortcuts import render

from django.views import View
from django.contrib import messages

from apps.base.models import SubEmail
from .models import Country


class HomeView(View):
    """
    View to handle home page.
    """

    def get(self, request, *args, **kwargs):
        countries = Country.objects.filter(is_active=True)

        context = {
            'countries': countries.order_by('name')[:10],
        }

        return render(request, 'home.html', context)

    def post(self, request, *args, **kwargs):
        countries = Country.objects.filter(is_active=True)

        search = request.POST.get('query')
        sub_email = request.POST.get('sub_email')

        if search:
            countries = Country.objects.filter(
                name__icontains=search, is_active=True)

        if sub_email:
            if SubEmail.objects.filter(email=sub_email).exists():
                messages.error(request, 'Email already exists')
            else:
                SubEmail.objects.create(email=sub_email)
                messages.success(request, 'Email added successfully')
        else:
            messages.error(request, 'Please enter email')

        context = {
            'countries': countries.order_by('name')[:10],
        }

        return render(request, 'home.html', context)
