from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from apps.Core import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('prof/home/', views.homeprof, name = 'homeprof'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.home, name='profile'),
    path('logout/', views.exit, name='logout'),

    # Urls del Cambio de contraseña
    path('sendChange/', views.CustomPasswordResetView.as_view(), name = 'sendchange'),
    path('doneChange/', auth_views.PasswordResetDoneView.as_view(template_name="Auth/donechange.html"), name = 'donechange'),
    path('changePass/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="Auth/changepass.html"), name = 'changepass'),
    path('change/', auth_views.PasswordResetCompleteView.as_view(template_name="Auth/change.html"), name = 'change'),
    

    #asignatura (mont)
    path('Asignatura',views.asigantura_home,name="Asignatura"),
    path('Asignatura/crear',views.save_asignatura,name="Asignatura_crear"),
    #----------------

    #curso y paralelos (mont y renato)
    path('paralelo/<int:paralelo>/d',views.eliminacion_paralelo),
    path('paralelo/<int:paralelo>/m',views.modificar_paralelo),
    path('paralelo/generar',views.generacion_paralelo,name="generar_p"),
    path('Cursos_Paralelos/', views.Cursos_visualizacion, name="Curso"),
    path('edicion/<codigo>', views.edicion_curso, name="edicion"),
    path('projects/eliminar/<codigo>/', views.eliminar_curso, name='eliminar'),
    #-----------------------
    
    #foro
    path('foro/', views.foro, name='foro'),
    path('add_foro/', views.add_foro, name='add_foro'),
    path('add_discussion/<int:foro_id>/', views.add_discussion, name='add_discussion'),
    path('foro/delete_discussion/<int:foro_id>/', views.delete_discussion, name='delete_discussion'),
    
    #post-repo
    path('Asignatura/<pk>/repositorios/', views.repositorios_profesor, name='repositorios_profesor'),
    path('profesor/<pk>/repositorios/crear/', views.crearRepositorio, name='crear_repositorio'),
    path('repositorio/<str:usuario>/<str:name>/<pk>', views.RepositorioDetalleView.as_view(), name='repositorio_detalle'),
    path('repositorio/<pk>/crear-post/', views.crearPost, name='crear_post'),
    path('repositorio/eliminar/<pk>/', views.eliminarPost, name='eliminarPost'),
]

