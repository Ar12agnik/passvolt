"""passvolt URL Configuration

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
from django.urls import path
from PasswordManager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="home"),
    path('FAQ', views.FAQ,name="FAQ"),
    path('FAQlogin', views.FAQlogin,name="FAQlogin"),

    path('FAQlogin', views.FAQlogin,name="FAQlogin"),
    path('signup', views.signup,name="signup"),
    path('login', views.Ulogin,name="login"),
    path('home', views.after_login,name="login-home"),
    path('logout', views.logout_page_user,name="logout"),
    path('add_password', views.add_password,name="add-password"),
    path('generate_password_page', views.generate_password_page,name="generate_password_page"),
    path('delete/<int:pk>/', views.delete_pwd,name="delete_pwd"),
    path('update/<int:pk>/', views.update_pwd,name="update_pwd"),
    
]
