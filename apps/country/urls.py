from django.urls import path

from .views import HomeView, single_page_as_view


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('single-page/<uuid:uuid>/', single_page_as_view, name='single-page'),
]
