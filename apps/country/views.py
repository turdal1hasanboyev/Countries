from django.shortcuts import render, get_object_or_404, redirect

from django.views import View
from django.contrib import messages

from apps.base.models import SubEmail
from .models import Country


class HomeView(View):
    """
    View to handle home page.
    """

    def get(self, request, *args, **kwargs):
        search = request.GET.get('query')

        countries = Country.objects.filter(is_active=True).order_by('name')

        if search:
            countries = Country.objects.filter(
                name__icontains=search, is_active=True)

        context = {
            'countries': countries,
        }

        return render(request, 'home.html', context)

    def post(self, request, *args, **kwargs):
        sub_email = request.POST.get('sub_email')

        if sub_email:
            if SubEmail.objects.filter(email=sub_email).exists():
                messages.error(request, 'Email already exists')
            else:
                SubEmail.objects.create(email=sub_email)
                messages.success(request, 'Email added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Please enter email')
            return redirect('home')


class SinglePageView(View):
    """
    View to handle single page.
    """

    template_name = "single.html"

    def get(self, request, *args, **kwargs):
        uuid = kwargs.get('uuid')

        country = get_object_or_404(Country, uuid=uuid, is_active=True)

        context = {
            'country': country,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        url = request.build_absolute_uri()

        sub_email = request.POST.get('sub_email')

        if sub_email:
            if SubEmail.objects.filter(email=sub_email).exists():
                messages.error(request, 'Email already exists')
            else:
                SubEmail.objects.create(email=sub_email)
                messages.success(request, 'Email added successfully')
            return redirect(url)
        else:
            messages.error(request, 'Please enter email')
            return redirect(url)


single_page_as_view = SinglePageView.as_view()
