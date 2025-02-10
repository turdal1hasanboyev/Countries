from django.urls import path

from .views import ProfileView
from .logout import LogOutView


urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogOutView.as_view(), name='logout'),
]
