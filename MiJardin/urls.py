"""
URL configuration for MiJardin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('plantas.urls')), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),##para dar token de acceso
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),##para pedir un nuevo token

###le dice a Django:
###Las URLs de la aplicación plantas serán manejadas por el archivo plantas/urls.py.
]
