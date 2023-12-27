# Aplicación Web para Reservas de Servicios para Eventos 





## Descripción del proyecto

Este proyecto fue desarrollado de forma colaborativa como trabajo final del programa de aceleración de talentos de Alkemy, en la especialización en desarrollo web con Python y Django.

El proyecto consiste en el desarrollo de una aplicación web **base** y se tenía como caso de negocio una empresa que ofrece reservas de servicios para eventos. 

El trabajo se desarrollo a lo largo de 3 semanas y siguiendo la metodología ágil Scrum. Para el trabajo colaborativo utilizamos Jira, Git y GitHub. 

## Características Principales

### Entidades

- Cliente
- Empleado
- Servicio
- Coordinador
- Reserva de Servicio

### Funcionalidades 

- CRUD + listar para Cliente
- CRUD + listar para Empleado
- CRUD + listar para Servicio
- CRUD + listar para Coordinador
- CRUD + listar para Reserva de Servicio

**Nota**: la eliminación para Cliente, Empleado, Servicio y Coordinador es una eliminación lógica (se desactiva el registro, es decir, cambio el estado del registro pero no se elimina de la base de datos). Y la eliminación para Reserva de Servicio es una eliminación física (se elimina de la base de datos). 

- APIs para acceder a la información de todas las entidades.

## Tecnologías Utilizadas

- Python
- Django
- Rest Framework

## Capturas de Pantalla de la Aplicación Web

Página de inicio:

![image](https://github.com/fatimabelen/proyecto_python-django/assets/99991131/a455c876-7c19-40fa-ac9b-cb178437aadd)

Muestra de las funcionalidades con la entidad Cliente:

![image](https://github.com/fatimabelen/proyecto_python-django/assets/99991131/45db9805-ce0a-40df-96bd-c1550264e966)

![image](https://github.com/fatimabelen/proyecto_python-django/assets/99991131/3ea84b23-9c3b-43ea-b017-7d3f0a78ff19)

![image](https://github.com/fatimabelen/proyecto_python-django/assets/99991131/96852207-3883-4ccf-8e5d-0db9d867120a)

Listado de Rerservas de Servicios con la funcionalidad de eliminar:

![image](https://github.com/fatimabelen/proyecto_python-django/assets/99991131/7f1b7d70-5c22-48ad-9fff-08d9dacd4c9b)


## Instrucciones de Instalación

1. Clonar este repositorio: `git clone https://github.com/fatimabelen/proyecto_python-django.git`
2. Instalar las dependencias: `pip install -r requirements.txt`
3. Realizar las migraciones de la base de datos: `python manage.py migrate`
4. Ejecutar la aplicación: `python manage.py runserver`


