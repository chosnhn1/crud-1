"""
URL configuration

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
from django.urls import path, include
from rest_framework import routers
# from .views import UserViewSet
from .views import user_list, user_detail

router = routers.DefaultRouter()
# router.register(r'', UserViewSet, basename='user')
# router.register(r'', user_list)
# router.register(r'/{pk}',user_detail)
urlpatterns = [
    path('<int:pk>', user_detail),
    path('', user_list)
]

urlpatterns += router.urls
