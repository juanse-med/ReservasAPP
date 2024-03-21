from django.urls import path
from . import views


urlpatterns = [
    path('habitaciones/', views.habitaciones, name='habitaciones'),
    path('reservas/', views.reservas, name='reservas'),
    path('mis_reservas/', views.mis_reservas, name='mis_reservas'),
    path('', views.index, name='index'),
    path('reservar/<int:habitacion_id>/', views.reservar_habitacion, name='reservar_habitacion'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    path('cancelar_reserva/<int:reserva_id>/', views.cancelar_reserva, name='cancelar_reserva'),
] 
