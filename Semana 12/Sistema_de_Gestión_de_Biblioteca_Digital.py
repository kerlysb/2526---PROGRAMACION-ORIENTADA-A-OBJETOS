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