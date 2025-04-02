# Gestor de Inventario en Python

## Descripción del Proyecto
Este proyecto es un gestor de inventario desarrollado en Python, utilizando Programación Orientada a Objetos (POO) y almacenamiento de datos en formato JSON. Su objetivo es facilitar la administración de un inventario de productos mediante un menú interactivo que permite realizar operaciones comunes de gestión.

## Funcionalidades
El gestor de inventario cuenta con las siguientes funcionalidades:
- **Agregar Producto:** Permite registrar un nuevo producto pidiendo ID, nombre, descripción, stock y precio.
- **Mostrar Inventario:** Muestra la lista completa de productos registrados.
- **Buscar Producto:** Realiza una búsqueda por ID para mostrar los detalles de un producto específico.
- **Eliminar Producto:** Elimina un producto del inventario mediante su ID.
- **Salir:** Finaliza la ejecución del programa.

## Clases y Funciones
El proyecto utiliza clases y funciones para mantener una estructura modular y clara:

- **Clase Producto:** Representa un producto con atributos como ID, nombre, descripción, stock y precio. Incluye el método `to_dict` para convertir el objeto a un diccionario compatible con JSON.

- **Clase Inventario:** Gestiona la lista de productos y operaciones sobre el inventario:
  - `cargar_datos`: Lee el archivo JSON y carga los productos existentes.
  - `guardar_datos`: Guarda la lista de productos en el archivo JSON.
  - `agregar_producto`: Añade un producto nuevo al inventario.
  - `mostrar_inventario`: Muestra todos los productos registrados.
  - `buscar_producto`: Encuentra un producto por su ID.
  - `borrar_producto`: Elimina un producto por su ID si existe.

- **Clase Menu:** Controla la interacción con el usuario mediante un menú dinámico:
  - `ejecutar`: Muestra el menú principal y gestiona la selección del usuario.

- **Función limpiar_pantalla:** Limpia la consola según el sistema operativo (Windows o Unix).


## Notas Adicionales
- El archivo `inventario.json` se generará automáticamente para almacenar la información.
- El programa limpia la pantalla automáticamente (excepto al mostrar el inventario).

## Autor
Sebastian




