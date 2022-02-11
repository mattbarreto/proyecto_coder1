from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app_proyectoFinal.models import Atleta, Avatar, Entrenador, Rutina
from app_proyectoFinal.forms import AvatarFormulario, atleta_create, entrenador_create, rutina_create
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request, 'inicio.html', {'avatar_url': avatar_url})


def entrenador(request):

    return render(request, 'entrenadores.html')

#ATLETAS

def atleta(request):

    return render(request, 'atletas.html',
    {'lista_atletas': Atleta.objects.all()})


def atleta_alta(request):

    if request.method=='POST':
        formulario_atletas = atleta_create(request.POST)
        
        if formulario_atletas.is_valid():
            data = formulario_atletas.cleaned_data

            Atleta.objects.create(
                nombre=data['nombre'], 
                apellido=data['apellido'],
                disciplina=data['disciplina'],
                fecha_nacimiento=data['fecha_de_nacimiento'],
                ciudad_de_nacimiento=data['ciudad_de_nacimiento'],
                pais_de_nacimiento=data['pais_de_nacimiento'],
                altura=data['altura'], 
                peso=data['peso'], 
                email=data['email']
                )
            return redirect('Atletas')
    else:
        formulario_atletas = atleta_create()

    return render(request, 'atletas_form.html', {'formulario_at': formulario_atletas})

def atleta_delete(request, id_atleta):
    
    atleta = Atleta.objects.get(id=id_atleta)
    atleta.delete()
    return redirect('Atletas')

def atleta_update(request, id_atleta):
    atleta = Atleta.objects.get(id=id_atleta)

    if request.method == 'POST':
        formulario_atletas = atleta_create(request.POST)

        if formulario_atletas.is_valid():
            data = formulario_atletas.cleaned_data
                
            atleta.nombre = data['nombre']
            atleta.apellido=data['apellido']
            atleta.disciplina=data['disciplina']
            atleta.fecha_de_nacimiento=data['fecha_de_nacimiento']
            atleta.ciudad_de_nacimiento=data['ciudad_de_nacimiento']
            atleta.pais_de_nacimiento = data['pais_de_nacimiento']
            atleta.altura=data['altura']
            atleta.peso=data['peso']
            atleta.email=data['email']

            atleta.save()

            return redirect('Atletas')

    else:
        formulario_atletas = atleta_create(model_to_dict(atleta))
        
    return render(request, 'atletas_form.html', {'formulario_at': formulario_atletas})

def atleta_busqueda(request):

    return render(request, 'atletas_busqueda.html')

def atletas_ls(request):
    
    if request.GET['apellido']:
        
        apellido_buscado = request.GET['apellido']
        apellido_atleta = Atleta.objects.filter(apellido__icontains=apellido_buscado)

        return render(request, 'atletas_resultados_ls.html', {'apellido_atleta': apellido_atleta, 'query': apellido_buscado})

    else:

        respuesta = 'No enviaste datos'
        return HttpResponse(respuesta)

class atletaListView(ListView):
    model = Atleta
    template_name = 'atletas.html'
    context_object_name = 'lista_atletas'

class atletaDetailView(DetailView):
    model = Atleta
    template_name = 'atletas_ver.html'

class atletaCreateView(CreateView):
    model = Atleta
    success_url = reverse_lazy('Atletas')
    fields = ['nombre', 'apellido', 'disciplina', 'fecha_de_nacimiento', 'ciudad_de_nacimiento',
            'pais_de_nacimiento', 'altura', 'peso', 'email']
    template_name = 'atletas_formulario.html'

class atletaUpdateView(UpdateView):
    model = Atleta
    success_url = reverse_lazy('Atletas')
    fields = ['nombre', 'apellido', 'disciplina' ,'fecha_de_nacimiento', 'ciudad_de_nacimiento',
            'pais_de_nacimiento', 'altura', 'peso', 'email']
    template_name = 'atletas_formulario.html'

class atletaDeleteView(DeleteView):
    model = Atleta
    success_url = reverse_lazy('Atletas')
    template_name = 'atletas_confirm_delete.html'

#ENTRENADORES

def entrenador(request):

    return render(request, 'entrenadores.html',
    {'lista_entrenadores': Entrenador.objects.all()})


def entrenador_alta(request):

    if request.method == 'POST':
        formulario_entrenador = entrenador_create(request.POST)

        if formulario_entrenador.is_valid():
            data = formulario_entrenador.cleaned_data

            Entrenador.objects.create(
                nombre=data['nombre'],
                apellido=data['apellido'],
                fecha_nacimiento=data['fecha_de_nacimiento'],
                estudios=data['estudios'],
                especialidad=data['especialidad'],
                email=data['email']
            )
            return redirect('Entrenadores')
    else:
        formulario_entrenador = entrenador_create()

    return render(request, 'entrenadores_form.html', {'formulario_en': formulario_entrenador})


def entrenador_delete(request, id_entrenador):

    entrenador = Entrenador.objects.get(id=id_entrenador)
    entrenador.delete()
    return redirect('Entrenadores')


def entrenador_update(request, id_entrenador):
    entrenador = Entrenador.objects.get(id=id_entrenador)

    if request.method == 'POST':
        formulario_entrenador = entrenador_create(request.POST)

        if formulario_entrenador.is_valid():
            data = formulario_entrenador.cleaned_data

            entrenador.nombre = data['nombre']
            entrenador.apellido = data['apellido']
            entrenador.fecha_de_nacimiento = data['fecha_de_nacimiento']
            entrenador.estudios = data['estudios']
            entrenador.especialidad = data ['especialidad']
            entrenador.email = data['email']

            entrenador.save()

            return redirect('Entrenadores')

    else:
        formulario_entrenador = entrenador_create(model_to_dict(entrenador))

    return render(request, 'entrenadores_form.html', {'formulario_en': formulario_entrenador})


def entrenador_busqueda(request):

    return render(request, 'entrenadores_buscar.html')


def entrenadores_ls(request):

    if request.GET['apellido']:

        apellido_buscado = request.GET['apellido']
        apellido_entrenador = Entrenador.objects.filter(
            apellido__icontains=apellido_buscado)

        return render(request, 'entrenador_resultados_ls.html', {'apellido_entrenador': apellido_entrenador, 'query': apellido_buscado})

    else:

        respuesta = 'No enviaste datos'
        return HttpResponse(respuesta)

class EntrenadoresListView(ListView):
    model = Entrenador
    template_name = 'entrenadores.html'
    context_object_name = 'lista_entrenadores'

class EntrenadoresDetailView(DetailView):
    model = Entrenador
    template_name = 'entrenadores_ver.html'

class EntrenadoresCreateView(CreateView):
    model = Entrenador
    success_url = reverse_lazy('Entrenadores')
    fields = ['nombre', 'apellido', 'fecha_de_nacimiento', 'estudios', 'especialidad', 'email']
    template_name = 'entrenadores_formulario.html'

class EntrenadoresUpdateView(UpdateView):
    model = Entrenador
    success_url = reverse_lazy('Entrenadores')
    fields = ['nombre', 'apellido', 'fecha_de_nacimiento', 'estudios', 'especialidad', 'email']
    template_name = 'entrenadores_formulario.html'

class EntrenadoresDeleteView(DeleteView):
    model = Entrenador
    success_url = reverse_lazy('Entrenadores')
    template_name = 'entrenadores_confirm_delete.html'

#RUTINAS

def rutina(request):

    return render(request, 'rutinas.html', 
    {'lista_rutinas': Rutina.objects.all()})

def rutina_alta(request):
    if request.method == 'POST':
        formulario_rutinas = rutina_create(request.POST)

        if formulario_rutinas.is_valid():
            data = formulario_rutinas.cleaned_data

            Rutina.objects.create(
                nombre=data['nombre'],
                fecha_inicio=data['fecha_de_inicio'],
                intensidad=data['intensidad'],
                ejercicio_1=data['ejercicio_1'],
                ejercicio_2=data['ejercicio_2'],
                ejercicio_3=data['ejercicio_3'],
                ejercicio_4=data['ejercicio_4'],
                ejercicio_5=data['ejercicio_5'],
                ejercicio_6=data['ejercicio_6'],
                ejercicio_7=data['ejercicio_7'],
                duracionPorEjercicio=data['duración_por_ejercicio'],
                descansoEntreEjercicio=data['descanso_entre_ejercicio'],
                rondas=data['rondas'],
            )
            return redirect('Rutinas')
    else:
        formulario_rutinas = rutina_create()

    return render(request, 'rutinas_form.html', {'formulario_ruti': formulario_rutinas})


def rutinas_delete(request, id_rutinas):

    rutina = Rutina.objects.get(id=id_rutinas)
    rutina.delete()
    return redirect('Rutinas')


def rutina_update(request, id_rutinas):
    rutina = Rutina.objects.get(id=id_rutinas)

    if request.method == 'POST':
        formulario_rutinas = rutina_create(request.POST)

        if formulario_rutinas.is_valid():
            data = formulario_rutinas.cleaned_data

            rutina.nombre = data['nombre'],
            rutina.fecha_inicio = data['fecha de inicio'],
            rutina.intensidad = data['intensidad'],
            rutina.ejercicio_1 = data['ejercicio_1'],
            rutina.ejercicio_2 = data['ejercicio_2'],
            rutina.ejercicio_3 = data['ejercicio_3'],
            rutina.ejercicio_4 = data['ejercicio_4'],
            rutina.ejercicio_5 = data['ejercicio_5'],
            rutina.ejercicio_6 = data['ejercicio_6'],
            rutina.ejercicio_7 = data['ejercicio_7'],
            rutina.duracionPorEjercicio = data['duración_por_ejercicio'],
            rutina.descansoEntreEjercicio = data['descanso_entre_ejercicio'],
            rutina.rondas = data['rondas'],

            rutina.save()

            return redirect('Rutinas')

    else:
        formulario_rutinas = rutina_create(model_to_dict(rutina))

    return render(request, 'rutinas_form.html', {'formulario_ruti': formulario_rutinas})


def rutinas_busqueda(request):

    return render(request, 'rutinas_busqueda.html')


def buscar_rutina(request):

    if request.GET["nom"]:

        rut = request.GET["nom"]

        ruti = Rutina.objects.filter(nombre__icontains=rut)
        return render(request, "rutinasBusqueda.html", {"ruti": ruti, "query": rut})

    else:
        mensaje = "Por favor, introduzca un nombre para comenzar la búsqueda"
        

    return HttpResponse(mensaje)

class RutinasListView(ListView):
    model = Rutina
    template_name = 'rutinas.html'
    context_object_name = 'lista_rutinas'

class RutinasDetailView(DetailView):
    model = Rutina
    template_name = 'rutinas_ver.html'

class RutinasCreateView(CreateView):
    model = Rutina
    success_url = reverse_lazy('Rutinas')
    fields = ['nombre', 'fecha_inicio', 'intensidad', 'ejercicio_1', 'ejercicio_2', 'ejercicio_3', 'ejercicio_4', 'ejercicio_5', 'ejercicio_6', 'ejercicio_7', 'duracionPorEjercicio', 'descansoEntreEjercicio', 'rondas']
    template_name = 'rutinas_formulario.html'

class RutinasUpdateView(UpdateView):
    model = Rutina
    success_url = reverse_lazy('Rutinas')
    fields = ['nombre', 'fecha_inicio', 'intensidad', 'ejercicio_1', 'ejercicio_2', 'ejercicio_3', 'ejercicio_4', 'ejercicio_5', 'ejercicio_6', 'ejercicio_7', 'duracionPorEjercicio', 'descansoEntreEjercicio', 'rondas']
    template_name = 'rutinas_formulario.html'

class RutinasDeleteView(DeleteView):
    model = Rutina
    success_url = reverse_lazy('Rutinas')
    template_name = 'rutinas_confirm_delete.html'
    
    
# Avatar

def agregar_avatar(request):
    if request.method == 'POST':
        formulario = AvatarFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            avatar = Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return redirect('Inicio')
    else:   
        formulario = AvatarFormulario()
        
    return render(request, 'crear_avatar.html', {'form': formulario})
    