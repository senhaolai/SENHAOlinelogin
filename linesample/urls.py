"""
URL configuration for linesample project.

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
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # line login 
    path('accounts/', include('allauth.urls')),
    path('accounts/user_profile/', views.user_profile),
 
    # line pay  的請求和回調
    path('initiate_payment/', views.initiate_payment, name='initiate_payment'),
    path('confirm_payment/', views.confirm_payment, name='confirm_payment'),

    path('login/success/', views.login_success_view, name='login_success'),
]
