# Reservas App

Este proyecto consiste en una aplicación web para gestionar reservas de habitaciones de un hotel. Los usuarios pueden navegar por las habitaciones disponibles, realizar reservas, cancelarlas, y ver un listado de sus reservas activas.

## Cómo Ejecutar la Aplicación

1. **Clonar el Repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd nombre_de_tu_directorio
    ```

2. **Instalar Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configurar la Base de Datos:**
    Asegúrate de haber configurado tu base de datos en `settings.py`.

4. **Aplicar Migraciones:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Crear un Superusuario:**
    Si deseas acceder al panel de administración, crea un superusuario.
    ```bash
    python manage.py createsuperuser
    ```

6. **Ejecutar el Servidor:**
    ```bash
    python manage.py runserver
    ```

7. **Acceder a la Aplicación:**
    Ve a tu navegador web y visita `http://localhost:8000/`.

## Funcionamiento

### Página de Inicio (`/`)

La página de inicio muestra una breve introducción al sistema de reservas.

### Ver Habitaciones Disponibles (`/habitaciones/`)

En esta sección, los usuarios pueden explorar las habitaciones disponibles. Cada habitación muestra su número, tipo, precio por noche y una descripción.

### Realizar una Reserva (`/reservar/<int:habitacion_id>/`)

Los usuarios pueden reservar una habitación seleccionando la opción "Reservar" en la página de detalles de cada habitación disponible. Deben seleccionar las fechas de inicio y fin de la reserva. Después de confirmar la reserva, la habitación seleccionada se marca como no disponible hasta que la reserva se cancele.

### Ver Mis Reservas (`/mis_reservas/`)

Aquí, los usuarios pueden ver un listado de todas las reservas que han realizado. También tienen la opción de cancelar una reserva.

### Registrarse (`/signup/`) y Iniciar Sesión (`/login/`)

Los usuarios pueden registrarse para obtener una cuenta nueva o iniciar sesión con una cuenta existente.

### Cerrar Sesión (`/logout/`)

Los usuarios pueden cerrar sesión en sus cuentas activas.

### Cancelar una Reserva (`/cancelar_reserva/<int:reserva_id>/`)

Los usuarios pueden cancelar una reserva existente, lo que marcará la habitación como disponible nuevamente.


# Reservas_Hotel
