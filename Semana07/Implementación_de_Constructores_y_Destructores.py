import os
import tempfile


class GestorArchivo:
    """
    Clase que maneja la apertura y cierre de un archivo temporal.
    """

    def __init__(self, nombre_base):
        """
        Constructor: Inicializa el objeto creando un archivo temporal.
        Se activa al crear una instancia: obj = GestorArchivo('datos').
        """
        self.nombre_archivo = None
        self.fd = None
        try:
            # Crea un archivo temporal
            self.fd, self.nombre_archivo = tempfile.mkstemp(suffix='.txt', prefix=nombre_base)
            print(f"Archivo '{self.nombre_archivo}' creado e inicializado.")  # Mensaje de confirmación
        except Exception as e:
            print(f"Error en inicialización: {e}")

    def escribir(self, datos):
        """Método auxiliar para escribir datos en el archivo."""
        if self.fd:
            os.write(self.fd, datos)  # Corrección: datos ya es bytes

    def __del__(self):
        """
        Destructor: Cierra el archivo y lo elimina cuando el objeto se destruye.
        Se activa automáticamente cuando:
        - Se ejecuta 'del obj'
        - El objeto sale de scope (fin de función)
        - El recolector de basura libera el objeto (cuando referencias=0).
        """
        try:
            if self.fd:
                os.close(self.fd)
            if self.nombre_archivo and os.path.exists(self.nombre_archivo):
                os.remove(self.nombre_archivo)
            print(f"Archivo '{self.nombre_archivo}' cerrado y eliminado.")
        except Exception as e:
            print(f"Error en limpieza: {e}")


