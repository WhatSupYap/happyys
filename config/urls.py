"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from blog.views import hello_rest_api
from django.conf import settings
from common.images import get_image

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('api/hello/', hello_rest_api, name='hello_rest_api'),
    path('blog/', include('blog.urls')),
    path('common/', include('common.urls')),
    path('error/404', TemplateView.as_view(template_name='common/404.html'), name='error_404'),
    path('isg/', include('isg.urls')),
    path('samples/', include('samples.urls')),
    re_path(r'^images/(?P<path>.*)$', get_image, name='get_image'),
]

# 개발환경에서만 디버그 툴바 사용
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]