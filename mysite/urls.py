"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from jepa import views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = [
   path('admin/', admin.site.urls),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>', views.addition),
    path('base', views.base),
    path('lire', views.lire),
    path('',views.index),
    path('accueil/', views.accueil, name='accueil'),
    path('dons/', views.dons, name='dons'),
    path('archive/', views.archive, name='archive'),
    path('nousconnaitre/', views.nousconnaitre, name='nousconnaitre'),
    path('contact/', views.contact, name='contact'),
    path('chat/', views.chat, name='chat'),
    path('blog/', views.blog, name='blog')
   
   	
		
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
