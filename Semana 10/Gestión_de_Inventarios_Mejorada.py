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

    def to_file_line(self):
        """Formato para escribir en archivo: ID|nombre|cantidad|precio"""
        return f"{self._id}|{self._nombre}|{self._cantidad}|{self._precio}"

    @classmethod
    def from_file_line(cls, line):
        """Crear Producto desde línea de archivo"""
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
        """Guardar todos los productos en el archivo"""
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
        """Cargar productos desde el archivo"""
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
            return True  # No hay error, simplemente no existe
        except PermissionError:
            print(f"Error: No hay permisos para leer {self.archivo}")
            return False
        except Exception as e:
            print(f"Error al cargar inventario: {e}")
            return False

