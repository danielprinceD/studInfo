"""studInfo URL Configuration

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
from django.conf.urls import include,url
from django.urls import path
from depInfo import views
from cseStud import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dep/',views.depInfo),
    path('dep/cse/',include('cseStud.urls')),
    path('dep/ece/',include('eceStud.urls')),
    path('dep/eee/',include('eeeStud.urls')),
    path('dep/civil/',include('civilStud.urls')),
    path('dep/mech/',include('mechStud.urls')),

]
