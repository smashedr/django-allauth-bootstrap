from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from django.contrib import admin
from django_config.settings import STATIC_URL

import home.views as home

urlpatterns = [
    url(r'^$', home.home, name='home'),
    url(r'^favicon\.ico$', RedirectView.as_view(
        url=STATIC_URL + 'favicon.ico'
    )),
    url(r'^login/', home.login, name="login"),
    url(r'^oauth/', home.oauth_redirect, name="oauth"),
    url(r'^logout/', RedirectView.as_view(
        url='/accounts/logout/'
    ), name='logout'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls, name="django_admin"),
]
