import tkinter as tk
from tkinter import messagebox, Listbox, END, NORMAL, DISABLED


class AppListaTareas:
    def __init__(self, root):
        # Inicialización de la ventana principal con título descriptivo
        self.root = root
        self.root.title("Gestor de Lista de Tareas")
        self.root.geometry("500x400")

