from django.urls import path
from . import views 
from .views import lista_habitaciones, crear_habitacion, editar_habitacion, eliminar_habitacion
from .views import (
    lista_clientes, crear_cliente, editar_cliente, eliminar_cliente,
    lista_reservas, crear_reserva, editar_reserva, eliminar_reserva
)

urlpatterns = [
    path('', views.index, name='index'),
    path('habitaciones/', lista_habitaciones, name='lista_habitaciones'),
    path('habitaciones/nueva/', crear_habitacion, name='crear_habitacion'),
    path('habitaciones/<int:pk>/editar/', editar_habitacion, name='editar_habitacion'),
    path('habitaciones/<int:pk>/eliminar/', eliminar_habitacion, name='eliminar_habitacion'),

    # Clientes
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('clientes/nuevo/', crear_cliente, name='crear_cliente'),
    path('clientes/<int:pk>/editar/', editar_cliente, name='editar_cliente'),
    path('clientes/<int:pk>/eliminar/', eliminar_cliente, name='eliminar_cliente'),

    # Reservas
    path('reservas/', lista_reservas, name='lista_reservas'),
    path('reservas/nueva/', crear_reserva, name='crear_reserva'),
    path('reservas/<int:pk>/editar/', editar_reserva, name='editar_reserva'),
    path('reservas/<int:pk>/eliminar/', eliminar_reserva, name='eliminar_reserva'),

    path('login/', views.custom_login, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('logout-success/', views.logout_success, name='logout_success'),
]

