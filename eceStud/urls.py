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

urlpatterns = [
      
    path('year3/',views.year3),
    path('year3/profile3/<id>/',views.profile3),
    path('year3/update3/<int:id>/',views.update3),
    path('year3/delete3/<id>/',views.delete3),
    path('year3/create3/',views.create3),

    path('year4/',views.year4),
    path('year4/profile4/<id>/',views.profile4),
    path('year4/update4/<int:id>/',views.update4),
    path('year4/delete4/<id>/',views.delete4),
    path('year4/create4/',views.create4),
]
