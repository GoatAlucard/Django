"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from django.conf import settings 
from portafolio import views as portafolio_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index,name='index'),
    path('contacto/', core_views.contacto,name='contacto'),
    path('portafolio/', portafolio_views.portafolio, name='portafolio'),
    #path('acerca/', views.acerca, name='acerca')
    path('acerca', core_views.acerca, name='acerca')
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
