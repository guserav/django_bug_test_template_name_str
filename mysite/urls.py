"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import index, Broken_Template_View, broken_render_to_string, Working_Template_View, Potentially_Poisoned_Template_View

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('broken_template_view', Broken_Template_View.as_view()),
    path('working_template_view', Working_Template_View.as_view()),
    path('potentially_poisoned_view', Potentially_Poisoned_Template_View.as_view()),
    path('broken_render_to_string', broken_render_to_string),
]
