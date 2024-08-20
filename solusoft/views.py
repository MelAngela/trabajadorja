from django.shortcuts import render, get_object_or_404, redirect
from .forms import TrabajadorForm,CargasForm
from .models import Trabajador, Cargas
from django.http import HttpResponse


def listar_trabajadores(request):
    trabajadores = Trabajador.objects.all()
    return render(request, 'listar_trabajadores.html', {'trabajadores': trabajadores})

# Create your views here.


def detalle_trabajador(request, trabajador_id):
    trabajador = get_object_or_404(Trabajador, pk=trabajador_id)
    return render(request, 'detalle_trabajador.html', {'trabajador': trabajador})

def crear_trabajador(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_trabajadores')
    else:
        form = TrabajadorForm()
    return render(request, 'crear_trabajador.html', {'form': form})

def editar_trabajador(request, trabajador_id):
    trabajador = get_object_or_404(Trabajador, pk=trabajador_id)
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('detalle_trabajador', trabajador_id=trabajador_id)
    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, 'editar_trabajador.html', {'form': form, 'trabajador': trabajador})

# def buscar_trabajador(request):
#     if request.method == 'POST':
#         rut = request.POST.get('rut')  # Obtén el RUT desde el formulario
#         try:
#             trabajador = Trabajador.objects.get(rut=rut)  # Busca al trabajador por el RUT
#             return render(request, 'detalle_trabajador.html', {'trabajador': trabajador})
#         except Trabajador.DoesNotExist:
#             mensaje_error = "No se encontró un trabajador con ese RUT."
#             return render(request, 'error.html', {'mensaje_error': mensaje_error})

#     return render(request, 'buscar_trabajador.html')

def buscar_trabajador(request):
    mensaje_error = None

    if request.method == 'POST':
        rut = request.POST.get('rut')  # Obtén el RUT desde el formulario
        try:
            trabajador = Trabajador.objects.get(rut=rut)  # Busca al trabajador por el RUT
            return render(request, 'detalle_trabajador.html', {'trabajador': trabajador})
        except Trabajador.DoesNotExist:
            mensaje_error = "No se encontró un trabajador con ese RUT."

    return render(request, 'buscar_trabajador.html', {'mensaje_error': mensaje_error})


def eliminar_trabajador(request, trabajador_id):
    trabajador = get_object_or_404(Trabajador, pk=trabajador_id)
    if request.method == 'POST':
        trabajador.delete()
        return redirect('listar_trabajadores')
    return render(request, 'eliminar_trabajador.html', {'trabajador': trabajador})

def agregar_carga(request, trabajador_id):
    trabajador = get_object_or_404(Trabajador, id=trabajador_id)
    if request.method == 'POST':
        form = CargasForm(request.POST)
        if form.is_valid():
            carga = form.save(commit=False)
            carga.trabajador = trabajador
            carga.save()
            return redirect('detalle_trabajador', trabajador_id=trabajador_id)
    else:
        form = CargasForm()
    return render(request, 'agregar_carga.html', {'form': form, 'trabajador': trabajador})

def listar_cargas(request):
    trabajadores = Trabajador.objects.all()  # Obtener todos los trabajadores
    cargas_trabajadores = {}
    
    for trabajador in trabajadores:
        cargas = Cargas.objects.filter(trabajador=trabajador)  # Obtener las cargas de cada trabajador
        cargas_trabajadores[trabajador] = cargas
    
    return render(request, 'listar_cargas.html', {'cargas_trabajadores': cargas_trabajadores})


# def editar_carga(request, trabajador_id, carga_id):
#     trabajador = get_object_or_404(Trabajador, pk=trabajador_id)
#     carga = get_object_or_404(Cargas, pk=carga_id, trabajador=trabajador)
    
#     if request.method == 'POST':
#         form = CargasForm(request.POST, instance=carga)
#         if form.is_valid():
#             form.save()
#             return redirect('detalle_carga', trabajador_id=trabajador_id, carga_id=carga_id)
#     else:
#         form = CargasForm(instance=carga)
    
#     return render(request, 'editar_carga.html', {'form': form, 'trabajador': trabajador, 'carga': carga})

def editar_carga(request, trabajador_id, carga_id):
    trabajador = get_object_or_404(Trabajador, pk=trabajador_id)
    carga = get_object_or_404(Cargas, pk=carga_id, trabajador=trabajador)
    if request.method == 'POST':
        form = CargasForm(request.POST, instance=carga)
        if form.is_valid():
            form.save()
            return redirect('detalle_carga', trabajador_id=trabajador_id, carga_id =carga_id)
    else:
        form = CargasForm(instance=carga)
    return render(request, 'editar_carga.html', {'form': form, 'trabajador': trabajador, 'carga': carga})

def detalle_carga(request, trabajador_id, carga_id):
    carga = get_object_or_404(Cargas, pk=carga_id, trabajador_id=trabajador_id)
    return render(request, 'detalle_carga.html', {'carga': carga})

def eliminar_carga(request, trabajador_id, carga_id):
    trabajador = get_object_or_404(Trabajador, pk=trabajador_id)
    carga = get_object_or_404(Cargas, pk=carga_id, trabajador=trabajador)

    if request.method == 'POST':
        carga.delete()
        return redirect('eliminar_carga', trabajador_id=trabajador_id, carga_id=carga_id)  # Redirige al detalle del trabajador

    return render(request, 'eliminar_carga.html', {'trabajador': trabajador, 'carga':carga})

def buscar_trabajador_cargas(request):
    trabajador = None
    cargas = None

    if request.method == 'POST':
        rut = request.POST.get('rut')
        try:
            trabajador = Trabajador.objects.get(rut=rut)
            cargas = Cargas.objects.filter(trabajador=trabajador)
        except Trabajador.DoesNotExist:
            pass

    return render(request, 'buscar_trabajador_cargas.html', {'trabajador': trabajador, 'cargas': cargas})