"""musify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from music.views import *
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name = 'home'),
    path('music/', include('music.urls', namespace='music')),
    path('contact/', contact, name = 'contact'),
    path('terms/', terms, name = 'terms'),
    path('about_us/',    about_us, name = 'about_us'),
    path('add/', AddMusic, name='add'),
    path('add_music_submission/', add_music_submission, name='add_music_submission'),
    path('register/', register, name = 'register'),
    path('accounts/', include('allauth.urls')),
    path('add_admin/', AddMusic_admin, name='add_admin'),
    path('profile/', profile, name='profile'),
    path('', auth_views.LoginView.as_view(template_name = 'music/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'music/logout.html'), name = 'logout'),
]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
