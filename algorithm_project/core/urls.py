"""
URL configuration for konrix project.

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
from django.urls import path, include
from core.view import index_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", view=index_view, name="index"),

    #Apps
    path("apps/" , include("apps.urls")),

    #Custom
    path("custom/" , include("custom.urls")),

    # Layouts
    path("layouts/", include("layouts.urls")),

    #Elements
    path("elements/", include("elements.urls")),

    #Docs
    path("docs/", include("documentation.urls"))


]
