import json
from typing import Dict

class Producto:
    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self) -> str:
        return self.__id_producto

    def get_nombre(self) -> str:
        return self.__nombre

    def get_cantidad(self) -> int:
        return self.__cantidad

    def get_precio(self) -> float:
        return self.__precio

    # Setters
    def set_cantidad(self, cantidad: int):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print("La cantidad no puede ser negativa.")

    def set_precio(self, precio: float):
        if precio >= 0:
            self.__precio = precio
        else:
            print("El precio no puede ser negativo.")

    def __str__(self) -> str:
        return f"ID: {self.__id_producto} | Nombre: {self.__nombre} | " \
               f"Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"
class Inventario:
    def __init__(self, archivo: str = "inventario.txt"):
        self.__productos: Dict[str, Producto] = {}
        self.__archivo = archivo
        self.cargar_inventario()

    def agregar_producto(self, producto: Producto):
        if producto.get_id() in self.__productos:
            print("ERROR: Ya existe un producto con ese ID.")
        else:
            self.__productos[producto.get_id()] = producto
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto: str):
        if id_producto in self.__productos:
            del self.__productos[id_producto]
            print("Producto eliminado.")
        else:
            print("ERROR: No se encontró un producto con ese ID.")

    def actualizar_cantidad(self, id_producto: str, nueva_cantidad: int):
        if id_producto in self.__productos:
            self.__productos[id_producto].set_cantidad(nueva_cantidad)
            print("Cantidad actualizada.")
        else:
            print("ERROR: Producto no encontrado.")

    def actualizar_precio(self, id_producto: str, nuevo_precio: float):
        if id_producto in self.__productos:
            self.__productos[id_producto].set_precio(nuevo_precio)
            print("Precio actualizado.")
        else:
            print("ERROR: Producto no encontrado.")

    def buscar_por_nombre(self, nombre: str):
        encontrados = []
        for prod in self.__productos.values():
            if nombre.lower() in prod.get_nombre().lower():
                encontrados.append(prod)
        if encontrados:
            print(f"Productos que contienen '{nombre}':")
            for p in encontrados:
                print(p)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_todos(self):
        if not self.__productos:
            print("El inventario está vacío.")
        else:
            print("\n--- INVENTARIO ACTUAL ---")
            for prod in self.__productos.values():
                print(prod)
