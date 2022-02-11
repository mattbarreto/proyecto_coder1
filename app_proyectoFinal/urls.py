from django import views
from django.urls import path
from app_proyectoFinal.views import agregar_avatar, inicio, atletas_ls, atleta_busqueda, atletaCreateView, atletaDetailView, atletaDeleteView, atletaListView, atletaUpdateView, entrenador_busqueda, entrenadores_ls, EntrenadoresCreateView, EntrenadoresDeleteView, EntrenadoresDetailView, EntrenadoresListView, EntrenadoresUpdateView, rutina, RutinasCreateView, RutinasDeleteView, RutinasDetailView, RutinasListView, RutinasUpdateView, rutinas_busqueda, buscar_rutina
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_required(inicio), name='Inicio'),
    #path('rutina', rutina, name='Rutinas'),
    # path('atletas', atleta, name='Atletas'),
    # path('atletas/add', atleta_alta, name='Formulario de Atletas'),
    # path('atletas/delete/<id_atleta>', atleta_delete, name = 'Borrar Atletas'),
    # path('atletas/update/<id_atleta>', atleta_update, name= 'Actualizar Atletas'),
    path('atletas', login_required(atletaListView.as_view()), name='Atletas'),
    path('atletas/detalle/<pk>', login_required(atletaDetailView.as_view()), name='Detalle Atletas'),
    path('atletas/add', login_required(atletaCreateView.as_view()), name='Formulario de Atletas'),
    path('atletas/update/<pk>', login_required(atletaUpdateView.as_view()), name='Actualizar Atletas'),
    path('atletas/delete/<pk>', login_required(atletaDeleteView.as_view()), name='Borrar Atletas'),
    path('atletas/buscar', login_required(atleta_busqueda), name='Busqueda de Atletas'),
    path('atletas/listar_busqueda', login_required(atletas_ls), name='Search'),
    # ENTRENADORES
    path('entrenadores', login_required(EntrenadoresListView.as_view()), name='Entrenadores'),
    path('entrenadores/detalle/<pk>', login_required(EntrenadoresDetailView.as_view()), name='Detalle Entrenadores'),
    path('entrenadores_add', login_required(EntrenadoresCreateView.as_view()), name='Formulario de Entrenadores'),
    path('entrenadores/update/<pk>', login_required(EntrenadoresUpdateView.as_view()), name='Actualizar Entrenadores'),
    path('entrenadores/delete/<pk>', login_required(EntrenadoresDeleteView.as_view()), name='Borrar Entrenadores'),
    path('entrenadores/buscar', login_required(entrenador_busqueda), name='Busqueda de Entrenadores'),
    path('entrenadores/listar_busqueda', login_required(entrenadores_ls), name='Search Entrenador'),
    
    # RUTINAS
    path('rutinas', login_required(RutinasListView.as_view()), name='Rutinas'),
    path('rutinas/detalle/<pk>', login_required(RutinasDetailView.as_view()), name='Detalle de Rutinas'),
    path('rutinas/add', login_required(RutinasCreateView.as_view()), name='Formulario de Rutinas'),
    path('rutinas/update/<pk>', login_required(RutinasUpdateView.as_view()), name='Actualizar Rutinas'),
    path('rutinas/delete/<pk>', login_required(RutinasDeleteView.as_view()), name='Borrar Rutinas'),
    path('rutinas/buscar', login_required(rutinas_busqueda), name='Busqueda de Rutinas'),
    path('buscar_rutina', login_required(buscar_rutina), name='Buscar Rutinas'),
    path('user/avatar/add', agregar_avatar, name='avatar_add'),
]