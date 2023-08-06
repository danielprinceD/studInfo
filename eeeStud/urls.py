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
from django.urls import path
from eeeStud import views 
from depInfo import views as depInfoViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.eee),
    path('year1/',views.year1),
    path('year1/profile/<id>/',views.profile),
    path('year1/update/<int:id>/',views.update),
    path('year1/delete/<id>/',views.delete),
      
    path('year1/create1/',views.create1),
    path('year1/create1/',views.create1),


]
