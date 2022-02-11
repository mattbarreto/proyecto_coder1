"""proyecto_coder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from proyecto_coder.settings import MEDIA_ROOT, MEDIA_URL

from proyecto_coder.views import editar_perfil, login_request, register
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app_proyectoFinal.urls')),
    # login/logout
    path('login', login_request, name='Login'),
    path('registro', register, name='Registro'),
    path('logout', LogoutView.as_view(template_name= 'logout.html'), name='logout'),
    path('user/edit', editar_perfil, name= 'editar_perfil') 
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
