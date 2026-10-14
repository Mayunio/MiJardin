from django.shortcuts import render, redirect
from .models import Planta
from .forms import PlantaForm #sirve para importar el formulario PlantaForm que nosotros creamos anteriormente en forms.py, para poder utilizarlo dentro de views.py.
## from .forms significa que desde el archivo forms.py que está dentro de mi aplicación plantas
## se cambia from django.shortcuts import render>from django.shortcuts import render, redirect
##from rest_framework.decorators import api_view ##Permite definir qué métodos HTTP acepta una vista de la API.

from rest_framework.response import Response  ##Permite devolver una respuesta desde la API, por ejemplo, en formato JSON.
from .serializers import PlantaSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

##secrea la vista index, render  muestra html
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def plantas(request):
    plantas = Planta.objects.all()###obtiene los registros de Planta desde nuestra base de datos.

    return render(request, 'plantas/index.html', {'plantas': plantas})
  #El primer plantas es el nombre que tendrá la variable dentro del HTML    ###variale plantas = Planta.objects.all()Esta variable contiene los registros obtenidos desde la base de datos.

def crear(request):
    formulario = PlantaForm(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        return redirect('plantas')

    return render(request, 'plantas/crear.html', {'formulario': formulario})  ##request.FILES or None en la creación para permitir que el formulario reciba la imagen subida.

def editar(request, id):
    planta = Planta.objects.get(id=id)
    formulario = PlantaForm(request.POST or None, request.FILES or None, instance=planta)

    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('plantas')

    return render(request, 'plantas/editar.html', {'formulario': formulario})

##Porque nuestro modelo se llama Planta y nuestro formulario PlantaForm.

def eliminar(request, id):
    planta = Planta.objects.get(id=id) ###Busca la planta que queremos eliminar mediante su id
    planta.delete()
    return redirect('plantas')


@api_view(['GET'])
def api_inicio(request):
    return Response({
        'mensaje': 'Bienvenido a la API de MiJardin'
    })


"""@api_view(['GET']) ## es solo consultar si mal no lo recuer##
def api_plantas(request):
    plantas = Planta.objects.all()
    serializer = PlantaSerializer(plantas, many=True)
    return Response(serializer.data)"""""


@api_view(['GET', 'POST']) ##post es crear plantas desde el cliente
@permission_classes([IsAuthenticated])  
def api_plantas(request):

    if request.method == 'GET':
        plantas = Planta.objects.all()
        serializer = PlantaSerializer(plantas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlantaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=201
            )

        return Response(
            serializer.errors,
            status=400
        )


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def api_detalle_planta(request, id):

    try:
        planta = Planta.objects.get(id=id)
    except Planta.DoesNotExist:
        return Response(
            {'error': 'La planta no existe'},
            status=404
        )

    if request.method == 'GET':
        serializer = PlantaSerializer(planta)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlantaSerializer(
            planta,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=400
        )

    elif request.method == 'DELETE':
        planta.delete()
        return Response(status=204)