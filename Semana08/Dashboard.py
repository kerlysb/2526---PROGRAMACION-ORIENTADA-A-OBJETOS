import os
import subprocess
import sys

def mostrar_codigo(ruta_script):
    # Muestra el código fuente de un script Python.
    # Adaptación: Ruta absoluta mejorada para Windows y PyCharm.
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {os.path.basename(ruta_script)} ---")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print(f"El archivo '{ruta_script}' no se encontró.")
        return None
    except UnicodeDecodeError:
        print("Error: El archivo no es UTF-8. Intenta con otro encoding.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    """
        Ejecuta un script Python.
        Adaptación para Windows (usuario en Win11): Usa subprocess.run sin ventana nueva para ejecución en foreground.
        Opcional: 'pythonw' para background. Agregado manejo de errores y confirmación.
        """
    try:
        python_exe = sys.executable
        # Para ejecución visible (foreground, output en consola actual):
        resultado = subprocess.run([python_exe, ruta_script], check=True, text=True, capture_output=False)
        print("Script ejecutado exitosamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error en ejecución: {e.stderr}")
    except FileNotFoundError:
        print("Python no encontrado. Verifica tu entorno PyCharm.")
    except Exception as e:
        print(f"Error al ejecutar el código: {e}")
        # Alternativa background (sin ventana): subprocess.Popen([python_exe.replace('python', 'pythonw'), ruta_script])


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    unidades = {
        '0': 'OOP Proyectos',  # Nueva unidad para asignaciones POO
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    while True:
        print("\n" + "=" * 50)
        print("Dashboard - Gestión de Proyectos Python (POO & Más)")
        print("=" * 50)
        for key in unidades:
            ruta_unidad = os.path.join(ruta_base, unidades[key])
            if os.path.exists(ruta_unidad):
                print(
                    f"{key} - {unidades[key]} ({len([f for f in os.listdir(ruta_unidad) if f.is_dir()])} subcarpetas)")
            else:
                print(f"{key} - {unidades[key]} (No encontrada - Crea la carpeta)")
        print("G - Git Status (en ruta base)")
        print("0 - Salir")

        eleccion = input("\nElige opción: ").strip().upper()
        if eleccion == '0':
            print("¡Hasta luego! Usa Git para versionar cambios.")
            break
        elif eleccion == 'G':
            try:
                resultado = subprocess.run(['git', 'status'], cwd=ruta_base, check=True, text=True, capture_output=True)
                print(resultado.stdout)
            except:
                print("Git no disponible o no es repo. Inicializa con 'git init'.")
        elif eleccion in unidades:
            ruta_unidad = os.path.join(ruta_base, unidades[eleccion])
            if os.path.exists(ruta_unidad):
                mostrar_sub_menu(ruta_unidad)
            else:
                print(f"Crea la carpeta '{unidades[eleccion]}' en {ruta_base}")
        else:
            print("Opción inválida. Por favor, intenta nuevamente.")

def mostrar_sub_menu(ruta_unidad):
    """Submenú de subcarpetas. Interfaz mejorada con conteo de scripts."""
    while True:
        sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]
        print(f"\nSubmenú - {os.path.basename(ruta_unidad)} ({len(sub_carpetas)} subcarpetas)")
        for i, carpeta in enumerate(sub_carpetas, 1):
            ruta_carp = os.path.join(ruta_unidad, carpeta)
            scripts = len([f.name for f in os.scandir(ruta_carp) if f.is_file() and f.name.endswith('.py')])
            print(f"{i} - {carpeta} ({scripts} scripts .py)")
        print("0 - Atrás")

        eleccion = input("Elige: ").strip()
        if eleccion == '0':
            break
        try:
            idx = int(eleccion) - 1
            if 0 <= idx < len(sub_carpetas):
                mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[idx]))
        except:
            print("Entrada inválida. Por favor, intenta nuevamente.")

def mostrar_scripts(ruta_sub_carpeta):
    """Lista y maneja scripts. Nueva opción 'E' para editar (abre en editor default)."""
    while True:
        scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]
        print(f"\nScripts en {os.path.basename(ruta_sub_carpeta)} ({len(scripts)})")
        for i, script in enumerate(scripts, 1):
            print(f"{i} - {script}")
        print("0 - Atrás | 9 - Menú Principal | E - Editar en PyCharm/Editor")

        eleccion = input("Elige: ").strip().upper()
        if eleccion == '0':
            break
        elif eleccion == '9':
            return
        elif eleccion == 'E':
            # Abre carpeta en explorer (Windows)
            os.startfile(os.path.dirname(ruta_sub_carpeta))
            continue
        try:
            idx = int(eleccion) - 1
            if 0 <= idx < len(scripts):
                ruta_script = os.path.join(ruta_sub_carpeta, scripts[idx])
                codigo = mostrar_codigo(ruta_script)
                if codigo:
                    ejecutar = input("\n¿Ejecutar? (S/N): ").strip().upper()
                    if ejecutar == 'S':
                        ejecutar_codigo(ruta_script)
                    input("\nPresiona Enter para continuar...")
        except:
            print("Entrada inválida. Por favor, intenta nuevamente")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
