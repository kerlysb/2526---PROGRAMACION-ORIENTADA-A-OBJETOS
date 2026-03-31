import tkinter as tk
from tkinter import messagebox, Listbox, END, NORMAL, DISABLED, SINGLE

class AppGestionTareas:
    def __init__(self, root):
        # Configuración ventana principal
        self.root = root
        self.root.title("Gestor de Tareas - Kerly Suarez")
        self.root.geometry("550x450")
        self.root.bind('<Escape>', lambda e: self.root.quit())  # Atajo Escape para cerrar

        # Lista de tareas: cada una es un dict {'texto': str, 'completada': bool}
        self.tareas = []

        # Frame principal
        main_frame = tk.Frame(root, padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')

        # Campo de entrada
        entry_frame = tk.Frame(main_frame)
        entry_frame.pack(pady=10)
        tk.Label(entry_frame, text="Nueva tarea:", font=("Arial", 12)).pack(side='left')
        self.entry = tk.Entry(entry_frame, font=("Arial", 12), width=30)
        self.entry.pack(side='left', padx=10)
        self.entry.bind('<Return>', lambda e: self.anadir_tarea())  # Enter para añadir
        self.entry.focus()

        # Frame de botones
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Añadir Tarea", command=self.anadir_tarea,
                  bg="#4CAF50", fg="white", activebackground="#9370DB", activeforeground="white",
                  relief="raised", borderwidth=5, font=("Arial", 10, "bold")).pack(side="left", padx=5)
        tk.Button(button_frame, text="Marcar Completada", command=self.marcar_completada,
                  bg="#2196F3", fg="white", activebackground="#9370DB", activeforeground="white",
                  relief="raised", borderwidth=5, font=("Arial", 10, "bold")).pack(side="left", padx=5)
        tk.Button(button_frame, text="Eliminar Tarea", command=self.eliminar_tarea,
                  bg="#f44336", fg="white", activebackground="#9370DB", activeforeground="white",
                  relief="raised", borderwidth=5, font=("Arial", 10, "bold")).pack(side="left", padx=5)

        # Listbox para mostrar tareas
        list_frame = tk.Frame(main_frame)
        list_frame.pack(expand=True, fill='both', pady=10)
        tk.Label(list_frame, text="Lista de Tareas:", font=("Arial", 12, "bold")).pack(anchor='w')
        self.listbox = Listbox(list_frame, font=("Arial", 11), selectmode=SINGLE, height=15)  # SINGLE para selección única [web:4][web:9]
        scrollbar = tk.Scrollbar(list_frame, orient="vertical")
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        self.listbox.pack(side="left", expand=True, fill='both')
        scrollbar.pack(side="right", fill="y")

        # Bind para atajos
        self.root.bind('c', lambda e: self.marcar_completada())  # C para completar (ignore case)
        self.root.bind('<Delete>', lambda e: self.eliminar_tarea())  # Delete para eliminar
        self.root.bind('d', lambda e: self.eliminar_tarea())  # D para eliminar
        self.listbox.bind('<<ListboxSelect>>', self.on_select)  # Actualiza selección

        # Mensaje inicial
        self.listbox.insert(END, "Añade tareas con enter, c para completar y d para eliminar")

    def anadir_tarea(self):
        texto = self.entry.get().strip()
        if not texto:
            messagebox.showwarning("Advertencia", "¡Escribe una tarea!")
            return
        self.tareas.append({'texto': texto, 'completada': False})
        self.actualizar_lista()
        self.entry.delete(0, END)
        self.entry.focus()

    def marcar_completada(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Advertencia", "¡Selecciona una tarea!")
            return
        idx = sel[0]
        self.tareas[idx]['completada'] = not self.tareas[idx]['completada']  # Toggle
        self.actualizar_lista()
        self.listbox.selection_set(idx)  # Re-selecciona

    def eliminar_tarea(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Advertencia", "¡Selecciona una tarea!")
            return
        idx = sel[0]
        del self.tareas[idx]
        self.actualizar_lista()

    def actualizar_lista(self):
        self.listbox.delete(0, END)
        for tarea in self.tareas:
            marca = "✓" if tarea['completada'] else "○"  # Feedback visual
            display = f"{marca} {tarea['texto']}"
            self.listbox.insert(END, display)

    def on_select(self, event):
        pass  # Placeholder para selección

if __name__ == "__main__":
    root = tk.Tk()
    app = AppGestionTareas(root)
    root.mainloop()