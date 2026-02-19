class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def to_string(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"

    def to_file_line(self):
        return f"{self._id}|{self._nombre}|{self._cantidad}|{self._precio}"

    @classmethod
    def from_file_line(cls, line):
        try:
            parts = line.strip().split('|')
            if len(parts) != 4:
                raise ValueError("Formato de línea inválido")
            id_prod, nombre, cantidad, precio = parts
            return cls(id_prod, nombre, int(cantidad), float(precio))
        except (ValueError, IndexError) as e:
            print(f"Error al leer línea del archivo: {line.strip()} - {e}")
            return None


class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                for producto in self.productos:
                    f.write(producto.to_file_line() + '\n')
            return True
        except PermissionError:
            print(f"Error: No hay permisos para escribir en {self.archivo}")
            return False
        except Exception as e:
            print(f"Error al guardar inventario: {e}")
            return False

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                for line_num, linea in enumerate(f, 1):
                    producto = Producto.from_file_line(linea)
                    if producto:
                        self.productos.append(producto)
            print(f"Inventario cargado exitosamente ({len(self.productos)} productos)")
            return True
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado. Se creará uno nuevo.")
            return True
        except PermissionError:
            print(f"Error: No hay permisos para leer {self.archivo}")
            return False
        except Exception as e:
            print(f"Error al cargar inventario: {e}")
            return False

    def agregar_producto(self, producto):
        for prod in self.productos:
            if prod.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return False

        self.productos.append(producto)
        if self.guardar_inventario():
            print("Producto agregado y guardado exitosamente en el archivo.")
        else:
            print("Producto agregado en memoria, pero fallo al guardar en archivo.")
        return True

    def eliminar_producto(self, id_producto):
        for i, prod in enumerate(self.productos):
            if prod.get_id() == id_producto:
                eliminado = self.productos.pop(i)
                if self.guardar_inventario():
                    print(f"Producto eliminado y archivo actualizado: {eliminado.to_string()}")
                else:
                    print(f"Producto eliminado en memoria, pero fallo al actualizar archivo: {eliminado.to_string()}")
                return True
        print("Producto no encontrado.")
        return False

    def actualizar_producto(self, id_producto):
        for prod in self.productos:
            if prod.get_id() == id_producto:
                print(f"Producto actual: {prod.to_string()}")
                opcion = input("¿Qué desea actualizar? (1: Cantidad, 2: Precio): ")

                try:
                    if opcion == "1":
                        nueva_cantidad = int(input("Nueva cantidad: "))
                        prod.set_cantidad(nueva_cantidad)
                        print("Cantidad actualizada.")
                    elif opcion == "2":
                        nuevo_precio = float(input("Nuevo precio: "))
                        prod.set_precio(nuevo_precio)
                        print("Precio actualizado.")
                    else:
                        print("Opción inválida.")
                        return True

                    if self.guardar_inventario():
                        print("Cambios guardados exitosamente en el archivo.")
                    else:
                        print("Cambios aplicados en memoria, pero fallo al guardar en archivo.")
                    return True
                except ValueError:
                    print("Error: Ingrese valores numéricos válidos.")
                    return True

        print("Producto no encontrado.")
        return False

    def buscar_por_nombre(self, nombre):
        encontrados = []
        for prod in self.productos:
            if nombre.lower() in prod.get_nombre().lower():
                encontrados.append(prod)

        if encontrados:
            print("\nProductos encontrados:")
            for prod in encontrados:
                print(prod.to_string())
        else:
            print("No se encontraron productos con ese nombre.")
        return encontrados

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("\n=== INVENTARIO COMPLETO ===")
        for prod in self.productos:
            print(prod.to_string())
        print("=" * 50)


def mostrar_menu():
    print("\n=== SISTEMA DE GESTIÓN DE INVENTARIOS MEJORADO ===")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar producto por ID")
    print("4. Buscar productos por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    print("-" * 50)


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_prod = input("ID del producto: ")
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_prod, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: Los valores de cantidad y precio deben ser numéricos.")

        elif opcion == "2":
            id_buscar = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_buscar)

        elif opcion == "3":
            id_buscar = input("ID del producto a actualizar: ")
            inventario.actualizar_producto(id_buscar)

        elif opcion == "4":
            nombre_buscar = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre_buscar)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("¡Gracias por usar el sistema de inventarios!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()




