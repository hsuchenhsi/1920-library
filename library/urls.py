"""
URL configuration for library1920 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from mysite import views as mv
from mytest import views as testv
from mysite.views import search_books,post_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mv.homepage, name="homepage"),
    path('post/<slug:slug>/', mv.showpost, name="showpost"),
    path('post/', mv.post_view, name="post_view"),
    path('test/', testv.index, name="test-new"),
    path('test/delpost/<int:pid>/', testv.delpost),
    path('test/contact', testv.contact),
    path('post2db/', testv.post2db),
    path('register/', testv.register),
    path('login/', testv.login, name='login'),
    path('profile/', testv.profile),
    path('search/', search_books, name='search_books'),
    path('post/<slug:slug>/', post_view, name='post_detail'),
]









