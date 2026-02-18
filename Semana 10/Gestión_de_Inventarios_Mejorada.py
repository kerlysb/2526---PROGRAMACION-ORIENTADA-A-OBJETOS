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


