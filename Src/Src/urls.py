"""Src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from posts import views

urlpatterns = [
	url(r'^create/$', views.posts_create),
	url(r'^detail/(?P<id>\d+)/$', views.posts_detail),
	url(r'^list/$', views.posts_list),
    url(r'^$', views.base),
	url(r'^delete/(?P<id>\d+)/$', views.posts_delete),
	url(r'^update/(?P<id>\d+)/$', views.posts_update),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)