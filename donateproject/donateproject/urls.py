"""donateproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from donateapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('login', login_user),
    path('offers', offers),
    path('register', register),
    path('logout',logout_user),
    path('specific_offer/<str:pk>',specific_offer,name="specific_offer"),
    path('add_offer',add_offer),
    path('my_offers/<str:username>',my_offers),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
