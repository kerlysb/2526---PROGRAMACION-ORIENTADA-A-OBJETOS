class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def to_string(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Verificar si ya existe un producto con el mismo ID
        for prod in self.productos:
            if prod.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return False

        self.productos.append(producto)
        print("Producto agregado exitosamente.")
        return True

    def eliminar_producto(self, id_producto):
        for i, prod in enumerate(self.productos):
            if prod.get_id() == id_producto:
                eliminado = self.productos.pop(i)
                print(f"Producto eliminado: {eliminado.to_string()}")
                return True
        print("Producto no encontrado.")
        return False
    def actualizar_producto(self, id_producto):
        for prod in self.productos:
            if prod.get_id() == id_producto:
                print(f"Producto actual: {prod.to_string()}")
                opcion = input("¿Qué deseas actualizar? (1: Cantidad, 2: Precio): ")

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
    print("\n=== SISTEMA DE GESTIÓN DE INVENTARIOS ===")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar producto por ID")
    print("4. Buscar productos por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    print("-" * 40)





