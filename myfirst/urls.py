"""myfirst URL Configuration

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
from os import setregid
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainapp.views import ArticleViewGet,ArticleGet, CategoryViewGet,CategoryGet


urlpatterns = [
    path('admin/', admin.site.urls),
    ############################################
    path('article-get/',ArticleViewGet.as_view()),
    path('article-get/<int:pk>/',ArticleGet.as_view()),
    path('article-put/<int:pk>/',ArticleGet.as_view()),
    path('article-delete/<int:pk>/',ArticleGet.as_view()),
    #######################################################
    path('category-get/',CategoryViewGet.as_view()),
    path('category-get/<int:pk>/',CategoryGet.as_view()),
    path('category-put/<int:pk>/',CategoryGet.as_view()),
    path('category-delete/<int:pk>/',CategoryGet.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)