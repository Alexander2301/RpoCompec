from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('', login_required(vista_inicio), name= 'vista_inicio'),
	path('lista_corredores/',login_required(vista_listar_corredor), name= 'vista_corredor'),
    path('lista_marca/',login_required(vista_listar_marca), name= 'vista_marca'),
    path('lista_competencia/',login_required(vista_listar_competencia), name= 'vista_competencia'),
    path('lista_bicicleta/',login_required(vista_listar_bicicleta), name= 'vista_bicicleta'),
    path('lista_categoria/',login_required(vista_listar_categoria), name= 'vista_categoria'),
    path('lista_nacionalidad/',login_required(vista_listar_nacionalidad), name= 'vista_nacionalidad'),
    path('agregar_corredor/',login_required(vista_agregar_corredor), name= 'vista_agregar_corredor'),
    path('agregar_bicicleta/',login_required(vista_agregar_bicicleta), name= 'vista_agregar_bicicleta'),
    path('ver_corredor/<int:id_cor>/',login_required(vista_ver_corredor), name='vista_ver_corredor'),
    path('ver_bicicleta/<int:id_bic>/',login_required(vista_ver_bicicleta), name='vista_ver_bicicleta'),
    path('editar_corredor/<int:id_cor>/',login_required(vista_editar_corredor), name= 'vista_editar_corredor'),
    path('eliminar_corredor/<int:id_cor>/', login_required(vista_eliminar_corredor),name='vista_eliminar_corredor'),
    path('editar_bicicleta/<int:id_bic>/',login_required(vista_editar_bicicleta), name= 'vista_editar_bicicleta'),
    path('eliminar_bicicleta/<int:id_bic>/', login_required(vista_eliminar_bicicleta),name='vista_eliminar_bicicleta'),
    path('accounts/login/',vista_login, name='vista_login'),
    path('logout/',login_required(user_logout),name='user_logout'),
    path('register/',vista_register, name='vista_register'),
    path('perfil/',login_required(view_perfil), name= 'url_perfil'),
    path('ws/corredores/',login_required(ws_corredores_vista), name='ws_corredores_vista'),
]