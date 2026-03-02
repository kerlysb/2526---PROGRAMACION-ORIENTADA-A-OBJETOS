from typing import Tuple, Dict, Set, List

class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        self._titulo_autor: Tuple[str, str] = (titulo, autor)  # Tupla inmutable
        self.categoria: str = categoria
        self.isbn: str = isbn

    def __str__(self) -> str:
        titulo, autor = self._titulo_autor
        return f"{titulo} por {autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"

class Usuario:
    def __init__(self, nombre: str, id_usuario: str):
        self.nombre: str = nombre
        self.id_usuario: str = id_usuario
        self.libros_prestados: List[str] = []  # Lista de ISBNs

    def __str__(self) -> str:
        return f"Usuario {self.nombre} (ID: {self.id_usuario}), prestados: {len(self.libros_prestados)}"

class Biblioteca:
    def __init__(self):
        self.libros: Dict[str, Libro] = {}  # ISBN -> Libro
        self.usuarios_ids: Set[str] = set()  # IDs únicos
        self.usuarios: Dict[str, Usuario] = {}  # ID -> Usuario

    def anadir_libro(self, libro: Libro) -> bool:
        if libro.isbn in self.libros:
            print(f"❌ Libro ISBN {libro.isbn} ya existe.")
            return False
        self.libros[libro.isbn] = libro
        print(f"✅ Añadido: {libro}")
        return True

    def quitar_libro(self, isbn: str) -> bool:
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"✅ Quitado ISBN {isbn}")
            return True
        print(f"❌ No existe ISBN {isbn}")
        return False

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if usuario.id_usuario in self.usuarios_ids:
            print(f"❌ Usuario ID {usuario.id_usuario} ya registrado.")
            return False
        self.usuarios_ids.add(usuario.id_usuario)
        self.usuarios[usuario.id_usuario] = usuario
        print(f"✅ Registrado: {usuario}")
        return True

    def dar_baja_usuario(self, id_usuario: str) -> bool:
        if id_usuario not in self.usuarios_ids:
            print(f"❌ Usuario {id_usuario} no existe.")
            return False
        # Devolver préstamos automáticos
        usuario = self.usuarios[id_usuario]
        for isbn in usuario.libros_prestados[:]:
            self.devolver_libro(isbn, id_usuario)
        del self.usuarios[id_usuario]
        self.usuarios_ids.remove(id_usuario)
        print(f"✅ Baja de {id_usuario}")
        return True

    def prestar_libro(self, isbn: str, id_usuario: str) -> bool:
        if id_usuario not in self.usuarios_ids:
            print("❌ Usuario no registrado.")
            return False
        if isbn not in self.libros:
            print("❌ Libro no disponible.")
            return False
        self.usuarios[id_usuario].libros_prestados.append(isbn)
        print(f"✅ Prestado {isbn} a {id_usuario}")
        return True

    def devolver_libro(self, isbn: str, id_usuario: str) -> bool:
        if id_usuario not in self.usuarios_ids:
            return False
        usuario = self.usuarios[id_usuario]
        if isbn in usuario.libros_prestados:
            usuario.libros_prestados.remove(isbn)
            print(f"✅ Devuelto {isbn} de {id_usuario}")
            return True
        print(f"❌ {isbn} no prestado a {id_usuario}")
        return False

    def buscar_libros(self, criterio: str, valor: str) -> List[Libro]:
        resultados: List[Libro] = []
        for libro in self.libros.values():
            titulo, autor = libro._titulo_autor
            if (criterio == "titulo" and valor.lower() in titulo.lower()) or \
               (criterio == "autor" and valor.lower() in autor.lower()) or \
               (criterio == "categoria" and valor.lower() == libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def listar_prestados_usuario(self, id_usuario: str) -> List[Libro]:
        if id_usuario not in self.usuarios_ids:
            return []
        usuario = self.usuarios[id_usuario]
        return [self.libros[isbn] for isbn in usuario.libros_prestados if isbn in self.libros]

def menu(biblio: Biblioteca):
    while True:
        print("\n=== BIENVENID@ A LA BIBLIOTECA DIGITAL ===")
        print(" ¿Qué te gustaría hacer hoy?")
        print("1. Añadir libro      | 2. Quitar libro")
        print("3. Registrar usuario | 4. Dar baja usuario")
        print("5. Prestar libro     | 6. Devolver libro")
        print("7. Buscar libros     | 8. Listar prestados de usuario")
        print("0. Salir")
        opcion = input("Selecciona una opción del menú: ").strip()

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            cat = input("Categoría: ")
            isbn = input("ISBN: ")
            biblio.anadir_libro(Libro(titulo, autor, cat, isbn))
        elif opcion == "2":
            isbn = input("ISBN a quitar: ")
            biblio.quitar_libro(isbn)
        elif opcion == "3":
            nombre = input("Nombre: ")
            idu = input("ID único: ")
            biblio.registrar_usuario(Usuario(nombre, idu))
        elif opcion == "4":
            idu = input("ID a dar de baja: ")
            biblio.dar_baja_usuario(idu)
        elif opcion == "5":
            isbn = input("ISBN: ")
            idu = input("ID usuario: ")
            biblio.prestar_libro(isbn, idu)
        elif opcion == "6":
            isbn = input("ISBN: ")
            idu = input("ID usuario: ")
            biblio.devolver_libro(isbn, idu)
        elif opcion == "7":
            crit = input("Criterio (titulo/autor/categoria): ")
            val = input("Valor: ")
            for l in biblio.buscar_libros(crit, val):
                print(f"  - {l}")
        elif opcion == "8":
            idu = input("ID usuario: ")
            for l in biblio.listar_prestados_usuario(idu):
                print(f"  - {l}")
        elif opcion == "0":
            print("¡Gracias por visitar nuestra biblioteca digital, que tengas una feliz lectura!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    biblio = Biblioteca()
    menu(biblio)
