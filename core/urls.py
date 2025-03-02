"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # admin
from django.urls import path, include, re_path  # default url handler

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve  # media and static

from django.conf.urls import handler404
from .errors import PageNotFoundView  # page not found view


urlpatterns = [
    path('country/', admin.site.urls),  # admin path

    # media and static
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),

    # local path
    path("", include("apps.account.urls")),
    path("", include("apps.contact.urls")),
    path("", include("apps.country.urls")),
    path("", include("apps.base.urls")),
]

# static and media

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# error page settings

handler404 = PageNotFoundView.as_view()
