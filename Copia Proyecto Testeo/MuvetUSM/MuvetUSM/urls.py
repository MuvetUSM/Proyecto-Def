from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from apps.Core import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('prof/home/', views.homeprof, name = 'homeprof'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('loogin/', views.CustomLogintView.as_view(), name='login'),
    path('accounts/profile/', views.home, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('sendChange/', auth_views.PasswordResetView.as_view(template_name="Auth/sendchange.html", form_class=views.resetForm), name = 'sendchange'),
    path('doneChange/', auth_views.PasswordResetDoneView.as_view(template_name="Auth/donechange.html"), name = 'donechange'),
    path('changePass/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="Auth/changepass.html"), name = 'changepass'),
    path('change/', auth_views.PasswordResetCompleteView.as_view(template_name="Auth/change.html"), name = 'change'),
    
    path('cursos_paralelos',views.cursos_home,name='gestor'), 
    path('curso/<int:curso>/d',views.eliminacion_curso),
    path('curso/<int:curso>/m',views.modificar_curso),
    path('curso/generar',views.generacion_curso,name="generar_c"),
    path('paralelo/<int:paralelo>/d',views.eliminacion_paralelo),
    path('paralelo/generar',views.generacion_paralelo,name="generar_p"),
    path('inicio',views.inicio,name='inicio'), #home de la sesion
    
    path('Asiganturas/', views.Asignatura_vista, name="Asignatura"),
    path('edicion/<name>', views.edicion_asignatura, name="edicion"),
    path('projects/eliminar/<name>/', views.eliminar_asignatura, name='eliminar'),
]

