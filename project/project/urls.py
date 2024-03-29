"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from app2 import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.HomePage, name = 'home'),
    path('<int:id>', views.get, name = 'detail'),
    path('add/', views.Add_page, name = 'add'),
    path('', views.SignupPage, name = 'signup'),
    path('login/', views.LoginPage, name = 'login'),
    path('profile/', views.profile, name = 'profile'),
    path('logout/', views.LogoutPage, name = 'logout'),
    path('adminPage/', views.adminPage, name='adminPage'),
    path('profAdmin/', views.profAdmin, name='profAdmin'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('profEdit/', views.profEdit, name='profEdit'),
    path('updateProf/<str:id>', views.updateProf, name='updateProf'),
    path('deleteProf/<str:id>', views.deleteProf, name='deleteProf'),
    path('filterPrice/', views.filterPrice, name='filterPrice'),
    # path('car_search/', views.car_search, name='car_search'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
