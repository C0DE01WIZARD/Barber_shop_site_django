"""barber_shop URL Configuration

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
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from hair.views import index_page, Index_View, index_app

router = SimpleRouter()  # ПУТЬ ДЛЯ API
router.register('api/hairs', Index_View)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hair.urls')),
    path('', index_page),  # '' - переход на главную страницу
    path('index_app/', index_app)
]

urlpatterns += router.urls
