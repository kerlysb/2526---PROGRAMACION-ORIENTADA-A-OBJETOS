from typing import Tuple, Dict, Set, List
import json
import os


class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        self._titulo_autor: Tuple[str, str] = (titulo, autor)
        self.categoria: str = categoria
        self.isbn: str = isbn

    def __str__(self) -> str:
        titulo, autor = self._titulo_autor
        return f"{titulo} por {autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"

    def to_dict(self) -> dict:
        titulo, autor = self._titulo_autor
        return {"titulo": titulo, "autor": autor, "categoria": self.categoria, "isbn": self.isbn}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["titulo"], data["autor"], data["categoria"], data["isbn"])


class Usuario:
    def __init__(self, nombre: str, id_usuario: str):
        self.nombre: str = nombre
        self.id_usuario: str = id_usuario
        self.libros_prestados: List[str] = []

    def __str__(self) -> str:
        return f"Usuario {self.nombre} (ID: {self.id_usuario}), prestados: {len(self.libros_prestados)}"

    def to_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "id_usuario": self.id_usuario,
            "libros_prestados": self.libros_prestados
        }

    @classmethod
    def from_dict(cls, data: dict):
        usuario = cls(data["nombre"], data["id_usuario"])
        usuario.libros_prestados = data["libros_prestados"]
        return usuario


class Biblioteca:
    def __init__(self, archivo_libros: str = "libros.json", archivo_usuarios: str = "usuarios.json"):
        self.libros: Dict[str, Libro] = {}
        self.usuarios_ids: Set[str] = set()
        self.usuarios: Dict[str, Usuario] = {}
        self.archivo_libros = archivo_libros
        self.archivo_usuarios = archivo_usuarios
        self.cargar_datos()

    def guardar_datos(self):
        # Guardar libros
        libros_data = {isbn: libro.to_dict() for isbn, libro in self.libros.items()}
        with open(self.archivo_libros, "w", encoding="utf-8") as f:
            json.dump(libros_data, f, ensure_ascii=False, indent=2)

        # Guardar usuarios
        usuarios_data = {id_u: usuario.to_dict() for id_u, usuario in self.usuarios.items()}
        with open(self.archivo_usuarios, "w", encoding="utf-8") as f:
            json.dump(usuarios_data, f, ensure_ascii=False, indent=2)
        print(f"💾 Datos guardados en {self.archivo_libros} y {self.archivo_usuarios}")

    def cargar_datos(self):
        # Cargar libros
        if os.path.exists(self.archivo_libros):
            try:
                with open(self.archivo_libros, "r", encoding="utf-8") as f:
                    libros_data = json.load(f)
                    for isbn, data in libros_data.items():
                        self.libros[isbn] = Libro.from_dict(data)
                print(f"📚 Cargados {len(self.libros)} libros desde {self.archivo_libros}")
            except:
                print("⚠️ Error cargando libros, inicio vacío")

        # Cargar usuarios
        if os.path.exists(self.archivo_usuarios):
            try:
                with open(self.archivo_usuarios, "r", encoding="utf-8") as f:
                    usuarios_data = json.load(f)
                    for id_u, data in usuarios_data.items():
                        usuario = Usuario.from_dict(data)
                        self.usuarios[id_u] = usuario
                        self.usuarios_ids.add(id_u)
                        # Validar préstamos
                        usuario.libros_prestados = [isbn for isbn in usuario.libros_prestados if isbn in self.libros]
                print(f"👥 Cargados {len(self.usuarios)} usuarios desde {self.archivo_usuarios}")
            except:
                print("⚠️ Error cargando usuarios, inicio vacío")

    def anadir_libro(self, libro: Libro) -> bool:
        if libro.isbn in self.libros:
            print(f"❌ Libro ISBN {libro.isbn} ya existe.")
            return False
        self.libros[libro.isbn] = libro
        print(f"✅ Añadido: {libro}")
        return True

    def quitar_libro(self, isbn: str) -> bool:
        if isbn in self.libros:
            # Devolver préstamos automáticos
            for usuario in self.usuarios.values():
                if isbn in usuario.libros_prestados:
                    usuario.libros_prestados.remove(isbn)
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
        print("9. Guardar manual    | 0. Salir (guarda auto)")
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
