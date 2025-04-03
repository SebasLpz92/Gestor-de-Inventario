import json
import os
import platform

# Define el comando para limpiar la pantalla dependiendo del sistema operativo
clear_command = "cls" if platform.system() == "Windows" else "clear"

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system(clear_command)

# Clase que representa un Producto
class Producto:
    def __init__(self, id_producto, nombre, descripcion, stock, precio):
        # Inicializa los atributos del producto
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.stock = stock
        self.precio = precio

    # Convierte un objeto Producto en un diccionario
    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "stock": self.stock,
            "precio": self.precio
        }

# Clase que maneja el inventario de productos
class Inventario:
    def __init__(self, archivo_json="inventario.json"):
        # Inicializa el inventario con el archivo donde se almacenan los productos
        self.archivo_json = archivo_json
        self.productos = []
        self.cargar_datos()

    # Carga los productos desde el archivo JSON al inventario
    def cargar_datos(self):
        if os.path.exists(self.archivo_json):
            with open(self.archivo_json, 'r') as archivo:
                datos = json.load(archivo)
                self.productos = [Producto(**p) for p in datos]  # Crea objetos Producto desde el diccionario

    # Guarda los productos del inventario en un archivo JSON
    def guardar_datos(self):
        with open(self.archivo_json, 'w') as archivo:
            json.dump([p.to_dict() for p in self.productos], archivo, indent=4)

    # Agrega un nuevo producto al inventario y lo guarda
    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_datos()

    # Muestra todos los productos del inventario
    def mostrar_inventario(self):
        for p in self.productos:
            print(f"ID: {p.id_producto}, Nombre: {p.nombre}, Descripción: {p.descripcion}, Stock: {p.stock}, Precio: {p.precio}")

    # Busca un producto por su ID
    def buscar_producto(self, id_producto):
        for p in self.productos:
            if p.id_producto == id_producto:
                return p
        return None  # Devuelve None si no se encuentra el producto

    # Elimina un producto del inventario por su ID
    def borrar_producto(self, id_producto):
        producto = self.buscar_producto(id_producto)
        if producto:
            self.productos.remove(producto)
            self.guardar_datos()  # Guarda los cambios después de eliminar
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

# Clase que maneja el menú de interacción con el usuario
class Menu:
    def __init__(self):
        # Inicializa el inventario al crear el menú
        self.inventario = Inventario()

    # Ejecuta el bucle principal del menú
    def ejecutar(self):
        while True:
            print("\nGestor de Inventario:")
            print("1. Agregar producto")
            print("2. Mostrar inventario")
            print("3. Buscar producto")
            print("4. Borrar producto")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            # Opción 1: Agregar un producto
            if opcion == "1":
                limpiar_pantalla()
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                descripcion = input("Descripción: ")
                stock = int(input("Stock: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, descripcion, stock, precio)
                self.inventario.agregar_producto(producto)

            # Opción 2: Mostrar todos los productos del inventario
            elif opcion == "2":
                self.inventario.mostrar_inventario()

            # Opción 3: Buscar un producto por su ID
            elif opcion == "3":
                limpiar_pantalla()
                id_producto = input("Ingrese el ID del producto: ")
                producto = self.inventario.buscar_producto(id_producto)

                if producto:
                    print(f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Descripción: {producto.descripcion}, Stock: {producto.stock}, Precio: {producto.precio}")
                else:
                    print("Producto no encontrado.")

            # Opción 4: Eliminar un producto por su ID
            elif opcion == "4":
                limpiar_pantalla()
                id_producto = input("Ingrese el ID del producto a eliminar: ")
                self.inventario.borrar_producto(id_producto)

            # Opción 5: Salir del programa
            elif opcion == "5":
                limpiar_pantalla()
                print("Saliendo del gestor de inventario.")
                break

            # Si se ingresa una opción no válida
            else:
                limpiar_pantalla()
                print("Opción no válida.")

# Bloque principal para ejecutar el menú cuando se ejecuta el script
if __name__ == "__main__":
    Menu().ejecutar()
