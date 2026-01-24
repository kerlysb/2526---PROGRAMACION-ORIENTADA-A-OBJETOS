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

class ConexionDB:
    """
    Clase que simula una conexión a base de datos con limpieza.
    """

    def __init__(self, host):
        """
        Constructor: Inicializa la 'conexión' con el host proporcionado.
        """
        self.host = host
        self.conectado = True
        print(f"Conexión a {self.host} establecida.")

    def consultar(self):
        """Método auxiliar para simular una consulta."""
        if self.conectado:
            return "Datos consultados"
        return None

    def __del__(self):
        """
        Destructor: Cierra la conexión simulada.
        Se llama en las mismas condiciones que en GestorArchivo.
        """
        self.conectado = False
        print(f"Conexión a {self.host} cerrada correctamente.")

# Demostración del uso
if __name__ == "__main__":
    # Crear objetos: llama a __init__
    archivo = GestorArchivo("temp_datos")
    archivo.escribir(b"Datos de prueba\n")

    db = ConexionDB("localhost:5432")
    print(db.consultar())

    # Eliminar explícitamente: llama a __del__
    del archivo
    del db

    # El siguiente objeto se destruye al final del script (automático)
    temp = GestorArchivo("auto_temp")

    print("Programa ejecutado sin errores.")  # Confirmación final


