"""KACA URL Configuration

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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('mypage/', views.mypage, name='mypage'),
    path('category/', views.category, name='category'),
    path('academy/', views.academy, name='academy'),
    path('lecture_main/', views.lecture_main, name='lecture_main'),
    path('lecture_detail/', views.lecture_detail, name='lecture_detail'),
]
