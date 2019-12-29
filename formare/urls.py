"""formare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from apps.core import urls as formare_urls
from apps.accounts import urls as accounts_urls
from apps.clientes import urls as clientes_urls

from apps.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(formare_urls)),
    path('accounts/', include(accounts_urls)),
    path('cliente/', include(clientes_urls)),
    path('sitemap.xml',views.sitemap),
    
]