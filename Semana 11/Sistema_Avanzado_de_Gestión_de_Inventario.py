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

    # GUARDAR EN ARCHIVO TXT (formato: ID,nombre,cantidad,precio)
    def guardar_inventario(self):
        with open(self.__archivo, "w", encoding="utf-8") as f:
            for prod in self.__productos.values():
                linea = f"{prod.get_id()},{prod.get_nombre()},{prod.get_cantidad()},{prod.get_precio()}\n"
                f.write(linea)
        print(f"Inventario guardado en {self.__archivo}.")

    # CARGAR DESDE ARCHIVO TXT
    def cargar_inventario(self):
        try:
            with open(self.__archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue
                    partes = linea.split(",")
                    if len(partes) != 4:
                        continue
                    id_producto, nombre, cantidad_str, precio_str = partes
                    try:
                        cantidad = int(cantidad_str)
                        precio = float(precio_str)
                        p = Producto(id_producto, nombre, cantidad, precio)
                        self.__productos[id_producto] = p
                    except ValueError:
                        print(f"Ignorando línea mal formada: {linea}")
            print("Inventario cargado desde inventario.txt.")
        except FileNotFoundError:
            print("No se encontró archivo de inventario. Se iniciará uno vacío.")


# MENÚ INTERACTIVO
def menu():
    inventario = Inventario()

    while True:
        print("\n=== SISTEMA AVANZADO DE GESTIÓN DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad de producto")
        print("4. Actualizar precio de producto")
        print("5. Buscar producto por nombre")
        print("6. Mostrar todos los productos")
        print("7. Guardar y salir")
        print("0. Salir sin guardar")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            id_ = input("ID del producto: ").strip()
            nombre = input("Nombre del producto: ").strip()
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                p = Producto(id_, nombre, cantidad, precio)
                inventario.agregar_producto(p)
            except ValueError:
                print("Cantidad o precio inválido.")

        elif opcion == "2":
            id_ = input("ID del producto a eliminar: ").strip()
            inventario.eliminar_producto(id_)

        elif opcion == "3":
            id_ = input("ID del producto: ").strip()
            try:
                nueva = int(input("Nueva cantidad: "))
                inventario.actualizar_cantidad(id_, nueva)
            except ValueError:
                print("Cantidad inválida.")

        elif opcion == "4":
            id_ = input("ID del producto: ").strip()
            try:
                nuevo = float(input("Nuevo precio: "))
                inventario.actualizar_precio(id_, nuevo)
            except ValueError:
                print("Precio inválido.")

        elif opcion == "5":
            nombre = input("Nombre (o parte del nombre): ").strip()
            inventario.buscar_por_nombre(nombre)

        elif opcion == "6":
            inventario.mostrar_todos()

        elif opcion == "7":
            inventario.guardar_inventario()
            print("¡Hasta luego!")
            break

        elif opcion == "0":
            print("Saliendo sin guardar cambios.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
