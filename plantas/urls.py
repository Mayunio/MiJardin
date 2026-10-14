


##urlpatterns = [path('', views.index, name='index'), ##Cuando alguien entre a la dirección principal de MiJardin (/), ejecuta la función index de views.py.


from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('plantas', views.plantas, name='plantas'),
    path('plantas/crear', views.crear, name='crear'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('plantas/editar/<int:id>', views.editar, name='editar'),
    path('api/', views.api_inicio, name='api_inicio'),
    path('api/plantas/', views.api_plantas, name='api_plantas'),
    path('api/plantas/<int:id>/', views.api_detalle_planta, name='api_detalle_planta'),
    
    ]##apli/plantas la coleccion de plantas obvio 


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) ##static se importa para generar las rutas de las imágenes nuevas

