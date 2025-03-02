from django.urls import path

from .views import ProfileView
from .logout import LogOutView
from .login import LogInView
from .register import RegisterView


urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('login/', LogInView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
