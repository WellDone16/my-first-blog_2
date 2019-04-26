"""working_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include , re_path
from firstapp import views
from django.views.generic import ListView, DetailView
from news.models import Articles
urlpatterns = [

    #path('news/', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
    #template_name = "news/posts.html") ),

    path('admin/', admin.site.urls),
    path('', views.basic),
    path('slide_1', views.slide_1),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    


]
