"""TaxCreditDatabase URL Configuration

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
from TaxCreditDatabaseApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('usrd/', views.usrd, name='usrd'),
    path('sred/', views.sred, name='sred'),
    path('179d/', views.one79d, name='179d'),
    # path('credit_by_bc/', views.display_credit_by_bc, name='display_credit_by_bc'),
    path('display_usrd/', views.display_usrd_info, name= 'display_usrd')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




