import json
from typing import Dict

class Producto:
    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self) -> str:
        return self.__id_producto

    def get_nombre(self) -> str:
        return self.__nombre

    def get_cantidad(self) -> int:
        return self.__cantidad

    def get_precio(self) -> float:
        return self.__precio

    # Setters
    def set_cantidad(self, cantidad: int):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print("La cantidad no puede ser negativa.")

    def set_precio(self, precio: float):
        if precio >= 0:
            self.__precio = precio
        else:
            print("El precio no puede ser negativo.")

    def __str__(self) -> str:
        return f"ID: {self.__id_producto} | Nombre: {self.__nombre} | " \
               f"Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"
