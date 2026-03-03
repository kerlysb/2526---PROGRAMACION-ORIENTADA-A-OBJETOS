from typing import Tuple, Dict, Set, List
import os

class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        self._titulo_autor: Tuple[str, str] = (titulo, autor)  # TUPLA inmutable
        self.categoria: str = categoria
        self.isbn: str = isbn

    def __str__(self) -> str:
        titulo, autor = self._titulo_autor
        return f"{titulo} por {autor} ({self.categoria}) [{self.isbn}]"

    def to_txt(self) -> str:
        titulo, autor = self._titulo_autor
        return f"{titulo}|{autor}|{self.categoria}|{self.isbn}"

    @classmethod
    def from_txt(cls, linea: str):
        titulo, autor, categoria, isbn = linea.strip().split("|")
        return cls(titulo, autor, categoria, isbn)


class Usuario:
    def __init__(self, nombre: str, id_usuario: str):
        self.nombre: str = nombre
        self.id_usuario: str = id_usuario
        self.libros_prestados: List[str] = []  # Lista ISBNs

    def __str__(self) -> str:
        return f"{self.nombre} [{self.id_usuario}] - {len(self.libros_prestados)} libros"

    def to_txt(self) -> str:
        prestados = ",".join(self.libros_prestados)
        return f"{self.nombre}|{self.id_usuario}|{prestados}"

    @classmethod
    def from_txt(cls, linea: str):
        partes = linea.strip().split("|")
        nombre, id_usuario = partes[0], partes[1]
        prestados = partes[2].split(",") if len(partes) > 2 and partes[2] else []
        usuario = cls(nombre, id_usuario)
        usuario.libros_prestados = [isbn for isbn in prestados if isbn]
        return usuario


class Biblioteca:
    def __init__(self):
        self.libros: Dict[str, Libro] = {}
        self.usuarios_ids: Set[str] = set()
        self.usuarios: Dict[str, Usuario] = {}
        self.libros_txt = "libros_disponibles.txt"
        self.usuarios_txt = "usuarios_registrados.txt"
        self.historial_txt = "historial_prestamos.txt"
        self.cargar_todo()

    def guardar_historial_completo(self):
        """Guarda historial COMPLETO: préstamos activos"""
        try:
            with open(self.historial_txt, 'a', encoding='utf-8') as f:
                for id_usuario, usuario in self.usuarios.items():
                    for isbn in usuario.libros_prestados:
                        if isbn in self.libros:
                            linea = f"{id_usuario}|{usuario.nombre}|{isbn}|{self.libros[isbn]}|ACTIVO\n"
                            f.write(linea)
            print("    Historial actualizado (préstamos activos)")
        except Exception as e:
            print(f"    Error historial: {e}")

    def marcar_devuelto(self, isbn: str, id_usuario: str):
        """Marca préstamo como DEVUELTO en historial"""
        try:
            with open(self.historial_txt, 'a', encoding='utf-8') as f:
                linea_devuelta = f"{id_usuario}|{self.usuarios[id_usuario].nombre}|{isbn}|{self.libros[isbn]}|DEVUELTO\n"
                f.write(linea_devuelta)
            print("    Marcado como DEVUELTO en historial")
        except:
            pass

    def guardar_todo(self):
        """Guarda libros/usuarios + actualiza historial sin borrar viejo"""
        try:
            # 1. LIBROS DISPONIBLES (SÍ sobrescribe)
            with open(self.libros_txt, 'w', encoding='utf-8') as f:
                for libro in self.libros.values():
                    f.write(libro.to_txt() + '\n')

            # 2. USUARIOS REGISTRADOS (SÍ sobrescribe)
            with open(self.usuarios_txt, 'w', encoding='utf-8') as f:
                for usuario in self.usuarios.values():
                    f.write(usuario.to_txt() + '\n')

            # 3. HISTORIAL (APPEND - NO sobrescribe)
            self.guardar_historial_completo()

            print("  GUARDADO:")
            print(f"    {self.libros_txt}: {len(self.libros)} libros")
            print(f"    {self.usuarios_txt}: {len(self.usuarios)} usuarios")
            print(f"    {self.historial_txt}: histórico completo")
        except Exception as e:
            print(f" Error: {e}")

    def cargar_todo(self):
        print(" CARGANDO ARCHIVOS TXT...")
        # 1. LIBROS PRIMERO
        if os.path.exists(self.libros_txt):
            try:
                with open(self.libros_txt, 'r', encoding='utf-8') as f:
                    for linea in f:
                        if '|' in linea:
                            libro = Libro.from_txt(linea)
                            self.libros[libro.isbn] = libro
                print(f" Cargados {len(self.libros)} libros")
            except:
                pass
        # 2. USUARIOS
        if os.path.exists(self.usuarios_txt):
            try:
                with open(self.usuarios_txt, 'r', encoding='utf-8') as f:
                    for linea in f:
                        if '|' in linea:
                            usuario = Usuario.from_txt(linea)
                            self.usuarios[usuario.id_usuario] = usuario
                            self.usuarios_ids.add(usuario.id_usuario)
                print(f" Cargados {len(self.usuarios)} usuarios")
            except:
                pass

    def anadir_libro(self, libro: Libro) -> bool:
        if libro.isbn in self.libros:
            print(f" ISBN {libro.isbn} ya existe")
            return False
        self.libros[libro.isbn] = libro
        print(f" AÑADIDO: {libro}")
        return True

    def quitar_libro(self, isbn: str) -> bool:
        if isbn not in self.libros:
            print(f" ISBN {isbn} no existe")
            return False
        for usuario in self.usuarios.values():
            if isbn in usuario.libros_prestados:
                usuario.libros_prestados.remove(isbn)
        del self.libros[isbn]
        print(f" ELIMINADO: {isbn}")
        return True

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if usuario.id_usuario in self.usuarios_ids:
            print(f" ID {usuario.id_usuario} ya existe")
            return False
        self.usuarios_ids.add(usuario.id_usuario)
        self.usuarios[usuario.id_usuario] = usuario
        print(f" REGISTRADO: {usuario}")
        return True

    def dar_baja_usuario(self, id_usuario: str) -> bool:
        if id_usuario not in self.usuarios_ids:
            print(f" Usuario {id_usuario} no existe")
            return False
        self.usuarios[id_usuario].libros_prestados.clear()
        del self.usuarios[id_usuario]
        self.usuarios_ids.remove(id_usuario)
        print(f" BAJA: {id_usuario}")
        return True

    def prestar_libro(self, isbn: str, id_usuario: str) -> bool:
        if id_usuario not in self.usuarios_ids:
            print(f" Usuario {id_usuario} no registrado")
            return False
        if isbn not in self.libros:
            print(f" Libro {isbn} no disponible")
            return False
        self.usuarios[id_usuario].libros_prestados.append(isbn)
        print(f" PRESTADO: {self.libros[isbn]} → {self.usuarios[id_usuario].nombre}")
        return True

    def devolver_libro(self, isbn: str, id_usuario: str) -> bool:
        if id_usuario not in self.usuarios_ids:
            print(f" Usuario {id_usuario} no existe")
            return False
        usuario = self.usuarios[id_usuario]
        if isbn in usuario.libros_prestados:
            self.marcar_devuelto(isbn, id_usuario)
            usuario.libros_prestados.remove(isbn)
            print(f" DEVUELTO: {isbn}")
            return True
        print(f" {isbn} no prestado a {usuario.nombre}")
        return False

    def buscar_libros(self, criterio: str, valor: str) -> List[Libro]:
        resultados = []
        for libro in self.libros.values():
            titulo, autor = libro._titulo_autor
            if (criterio == "titulo" and valor.lower() in titulo.lower()) or \
                    (criterio == "autor" and valor.lower() in autor.lower()) or \
                    (criterio == "categoria" and valor.lower() == libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def listar_prestados(self, id_usuario: str) -> List[Libro]:
        if id_usuario not in self.usuarios_ids:
            return []
        usuario = self.usuarios[id_usuario]
        return [self.libros[isbn] for isbn in usuario.libros_prestados if isbn in self.libros]


def menu_interactivo():
    biblio = Biblioteca()

    while True:
        print(f"\n{'=' * 60}")
        print("      Bienvenido a nuestra Biblioteca Digital")
        print("         ¿Qué te gustaría hacer hoy?")
        print(f" LIBROS EXISTENTES: {len(biblio.libros)} |  USUARIOS: {len(biblio.usuarios)}")
        print("1️ AÑADIR LIBRO       |  2️ QUITAR LIBRO")
        print("3️ REGISTRAR USUARIO  |  4️ BAJA USUARIO")
        print("5️ PRESTAR LIBRO      |  6️ DEVOLVER LIBRO")
        print("7️ BUSCAR LIBROS      |  8️ MIS PRESTAMOS")
        print("9️ GUARDAR MANUAL     |  0️ SALIR (GUARDADO AUTOMÁTICO)")
        opcion = input("Selecciona una opción del menú: ").strip()

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblio.anadir_libro(Libro(titulo, autor, categoria, isbn))

        elif opcion == "2":
            isbn = input("ISBN a quitar: ")
            if isbn in biblio.libros:
                libro = biblio.libros[isbn]
                print(f" Usted esta eliminando: {libro}")
                confirm = input("Confirmar (s/n): ").lower().strip()
                if confirm == 's':
                    biblio.quitar_libro(isbn)
            else:
                print(f" ISBN {isbn} no encontrado")

        elif opcion == "3":
            nombre = input("Nombre: ")
            id_usuario = input("ID único: ")
            if id_usuario in biblio.usuarios_ids:
                print(f" ¡ID '{id_usuario}' YA ESTÁ REGISTRADO!")
                print(f"   Usuario actual: {biblio.usuarios[id_usuario].nombre}")
            else:
                biblio.registrar_usuario(Usuario(nombre, id_usuario))

        elif opcion == "4":
            id_usuario = input("ID usuario: ")
            if id_usuario in biblio.usuarios_ids:
                usuario = biblio.usuarios[id_usuario]
                print(f"  Eliminando usuario: {usuario}")
                print(f"    Préstamos actuales: {len(usuario.libros_prestados)}")
                confirm = input("Confirmar baja (s/n): ").lower().strip()
                if confirm == 's':
                    biblio.dar_baja_usuario(id_usuario)
            else:
                print(f" ID '{id_usuario}' no encontrado")

        elif opcion == "5":
            isbn = input("ISBN: ")
            id_usuario = input("ID usuario: ")
            biblio.prestar_libro(isbn, id_usuario)

        elif opcion == "6":
            isbn = input("ISBN: ")
            id_usuario = input("ID usuario: ")
            if id_usuario in biblio.usuarios_ids and isbn in biblio.usuarios[id_usuario].libros_prestados:
                usuario = biblio.usuarios[id_usuario]
                libro = biblio.libros[isbn]
                print(f"USTED ESTA DEVOLVIENDO:")
                print(f"    Libro: {libro}")
                print(f"    Usuario: {usuario.nombre} [{id_usuario}]")
                confirm = input("Confirmar devolución (s/n): ").lower().strip()
                if confirm == 's':
                    biblio.devolver_libro(isbn, id_usuario)
            else:
                print(f" ERROR: ISBN {isbn} no prestado a {id_usuario}")


        elif opcion == "7":
            valor = input("Buscar por TÍTULO: ").strip()
            resultados = biblio.buscar_libros("titulo", valor)
            print(f"\n {len(resultados)} resultado(s) por título:")
            if resultados:
                for libro in resultados:
                    print(f"    {libro}")
            else:
                print("   No se encontraron libros con ese título")

        elif opcion == "8":
            id_usuario = input("Tu ID: ")
            prestamos = biblio.listar_prestados(id_usuario)
            print(f"\n Tus préstamos ({len(prestamos)}):")
            for libro in prestamos:
                print(f"   {libro}")

        elif opcion == "9":
            biblio.guardar_todo()

        elif opcion == "0":
            biblio.guardar_todo()
            print("\n ¡Gracias! Los datos han sido guardados exitosamente")
            break

        else:
            print(" Opción inválida")

if __name__ == "__main__":
    menu_interactivo()
