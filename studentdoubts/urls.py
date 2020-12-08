"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('new',views.new,name='new'),
    path('sign',views.sign,name='sign'),
    path('signup',views.signup,name='signup'),
    path('slotbooking',views.slotbooking,name='slotbooking'),
    path('logout',views.logout,name='logout'),
    path('instantsolve',views.instantsolve,name='instantsolve'),
    path('videolinks',views.videolinks,name='videolinks'),
    path('science',views.science,name='science'),
    path('algebra',views.algebra,name='algebra'),
    path('geometry',views.geometry,name='geometry'),
    path('information',views.information,name='information'),
    path('videoscience',views.videoscience,name='videoscience'),
    path('videoalgebra',views.videoalgebra,name='videoalgebra'),
    path('videogeometry',views.videogeometry,name='videogeometry'),
    #path('videoinfo',views.videoinfo,name='videoinfo'),
    path('teacher',views.teacher,name='teacher'),
 
    
    
]
