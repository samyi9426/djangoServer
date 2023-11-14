"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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


# http://8.134.198.125:8000/
# http://8.134.198.125:8000/hellodjango/
# http://8.134.198.125:8000/api_a/
# http://8.134.198.125:8000/upload_file/
from django.contrib import admin
from django.urls import path
from myapp.views import index, hello, api_a
# urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('admin', admin.site.urls),
    path('hellodjango', hello, name='helloxxxxxxx'),
    path('api_a', api_a, name='api_axxxxxxx'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
