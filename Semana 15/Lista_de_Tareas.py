import tkinter as tk
from tkinter import messagebox, Listbox, END, NORMAL, DISABLED


class AppListaTareas:
    def __init__(self, root):
        # Inicialización de la ventana principal con título descriptivo
        self.root = root
        self.root.title("Gestor de Lista de Tareas")
        self.root.geometry("500x400")

        # Lista en memoria para almacenar las tareas (texto original y estado completado)
        self.tareas = []

        # Frame principal para organizar componentes verticalmente
        main_frame = tk.Frame(root)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

