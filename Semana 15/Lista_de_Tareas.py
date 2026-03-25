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

        # Campo de entrada para nuevas tareas con label explicativo
        tk.Label(main_frame, text="Nueva tarea:", font=("Arial", 12)).pack(anchor="w")
        self.entry = tk.Entry(main_frame, font=("Arial", 12), width=40)
        self.entry.pack(pady=5, fill="x")
        self.entry.focus()  # Foco automático en el entry para mejor UX
        # Evento de teclado: Enter para añadir tarea (bind <Return>)
        self.entry.bind("<Return>", lambda event: self.anadir_tarea())

        # Frame para botones de acción
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Añadir Tarea", command=self.anadir_tarea,
                  bg="#4CAF50", fg="white",
                  activebackground="#9370DB", activeforeground="white",
                  relief="raised", borderwidth=5,
                  font=("Arial", 10, "bold")).pack(side="left", padx=5)

        tk.Button(button_frame, text="Marcar Completada", command=self.marcar_completada,
                  bg="#2196F3", fg="white",
                  activebackground="#9370DB", activeforeground="white",
                  relief="raised", borderwidth=5,
                  font=("Arial", 10, "bold")).pack(side="left", padx=5)

        tk.Button(button_frame, text="Eliminar Tarea", command=self.eliminar_tarea,
                  bg="#f44336", fg="white",
                  activebackground="#9370DB", activeforeground="white",
                  relief="raised", borderwidth=5,
                  font=("Arial", 10, "bold")).pack(side="left", padx=5)

        # Listbox para mostrar tareas con scroll integrado

        list_frame = tk.Frame(main_frame)
        list_frame.pack(pady=10, fill="both", expand=True)

        self.listbox = Listbox(list_frame, font=("Arial", 11), height=15, selectmode="SINGLE")
        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scrollbar.set)

        self.listbox.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Evento de doble clic en Listbox para marcar como completada
        self.listbox.bind("<Double-1>", lambda event: self.marcar_completada())
        # <Double-1> es el evento estándar para doble clic izquierdo en Tkinter

    def anadir_tarea(self):
        """Añade la tarea del entry a la lista y actualiza visualmente."""
        texto = self.entry.get().strip()
        if texto:  # Validación: no añadir tareas vacías
            self.tareas.append((texto, False))  # Estado inicial: no completada
            self.actualizar_lista()
            self.entry.delete(0, END)  # Limpia el entry
            self.entry.focus()  # Regresa foco al entry
        else:
            messagebox.showwarning("Advertencia", "Escribe una tarea válida.")

    def marcar_completada(self):
        """Marca la tarea seleccionada como completada (cambia visualmente con visto)."""
        seleccion = self.listbox.curselection()
        if seleccion:
            index = seleccion[0]
            self.tareas[index] = (self.tareas[index][0], True)  # Cambia estado
            self.actualizar_lista()
            self.listbox.selection_clear(0, END)  # Limpia selección
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea.")

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada con confirmación."""
        seleccion = self.listbox.curselection()
        if seleccion:
            index = seleccion[0]
            if messagebox.askyesno("Confirmar", "¿Eliminar esta tarea?"):
                del self.tareas[index]
                self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea.")

    def actualizar_lista(self):
        """Actualiza el Listbox con prefijo visual para tareas completadas."""
        self.listbox.delete(0, END)
        for texto, completada in self.tareas:
            if completada:
                self.listbox.insert(END, f"✓ {texto}")  # Prefijo ✓ para completadas [web:42]
            else:
                self.listbox.insert(END, f"○ {texto}")  # Prefijo ○ para pendientes
        # Explicación: Actualización completa para evitar inconsistencias en la vista


if __name__ == "__main__":
    root = tk.Tk()
    app = AppListaTareas(root)
    root.mainloop()
