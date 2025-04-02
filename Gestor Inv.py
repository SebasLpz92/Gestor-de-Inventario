import json
import os
import platform

clear_command = "cls" if platform.system() == "Windows" else "clear"

def limpiar_pantalla():
    os.system(clear_command)

class Producto:
    def __init__(self, id_producto, nombre, descripcion, stock, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.stock = stock
        self.precio = precio

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "stock": self.stock,
            "precio": self.precio
        }

class Inventario:
    def __init__(self, archivo_json="inventario.json"):
        self.archivo_json = archivo_json
        self.productos = []
        self.cargar_datos()

    def cargar_datos(self):
        if os.path.exists(self.archivo_json):
            with open(self.archivo_json, 'r') as archivo:
                datos = json.load(archivo)
                self.productos = [Producto(**p) for p in datos]

    def guardar_datos(self):
        with open(self.archivo_json, 'w') as archivo:
            json.dump([p.to_dict() for p in self.productos], archivo, indent=4)

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_datos()

    def mostrar_inventario(self):
        for p in self.productos:
            print(f"ID: {p.id_producto}, Nombre: {p.nombre}, Descripción: {p.descripcion}, Stock: {p.stock}, Precio: {p.precio}")

    def buscar_producto(self, id_producto):
        for p in self.productos:
            if p.id_producto == id_producto:
                return p
        return None

    def borrar_producto(self, id_producto):
        producto = self.buscar_producto(id_producto)
        if producto:
            self.productos.remove(producto)
            self.guardar_datos()
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

class Menu:
    def __init__(self):
        self.inventario = Inventario()

    def ejecutar(self):
        while True:
            print("\nGestor de Inventario:")
            print("1. Agregar producto")
            print("2. Mostrar inventario")
            print("3. Buscar producto")
            print("4. Borrar producto")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                limpiar_pantalla()
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                descripcion = input("Descripción: ")
                stock = int(input("Stock: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, descripcion, stock, precio)
                self.inventario.agregar_producto(producto)
            elif opcion == "2":
                self.inventario.mostrar_inventario()
            elif opcion == "3":
                limpiar_pantalla()
                id_producto = input("Ingrese el ID del producto: ")
                producto = self.inventario.buscar_producto(id_producto)
                if producto:
                    print(f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Descripción: {producto.descripcion}, Stock: {producto.stock}, Precio: {producto.precio}")
                else:
                    print("Producto no encontrado.")
            elif opcion == "4":
                limpiar_pantalla()
                id_producto = input("Ingrese el ID del producto a eliminar: ")
                self.inventario.borrar_producto(id_producto)
            elif opcion == "5":
                limpiar_pantalla()
                print("Saliendo del gestor de inventario.")
                break
            else:
                limpiar_pantalla()
                print("Opción no válida.")

if __name__ == "__main__":
    Menu().ejecutar()