"""
URL configuration for rapidsaas project.

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
from django.urls import path, include

from .views import home_page_view, about_page_view, password_protected_view, login_required_view, staff_only_view
from auth import views as auth_views
from profiles import views as profile_views

urlpatterns = [
    path('', home_page_view, name='home'),
    path('about/', about_page_view),
    path('pw-protected/', password_protected_view),
    path('login-required/', login_required_view),
    path('staff-only/', staff_only_view),
    path('login/', auth_views.login_view),
    path('register/', auth_views.register_view),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profiles/', include('profiles.urls')),
]
