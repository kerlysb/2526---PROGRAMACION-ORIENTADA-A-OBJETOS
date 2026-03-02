from typing import Tuple, Dict, Set, List

class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        self._titulo_autor: Tuple[str, str] = (titulo, autor)  # Tupla inmutable
        self.categoria: str = categoria
        self.isbn: str = isbn

    def __str__(self) -> str:
        titulo, autor = self._titulo_autor
        return f"{titulo} por {autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"
