import tkinter as tk
from tkinter import ttk, messagebox
import calendar
import time


class DatePicker(tk.Toplevel):
    def __init__(self, widget=None):
        super().__init__()
        self.widget = widget
        self.title("Selector de Fecha")
        self.resizable(False, False)
        self.geometry("320x360+650+350")
        self.init_frames()
        self.init_needed_vars()
        self.init_month_year_labels()
        self.init_buttons()
        self.space_between_widgets()
        self.fill_days()
        self.make_calendar()

    def init_frames(self):
        self.frame1 = tk.Frame(self)
        self.frame1.pack(pady=10)
        self.frame_days = tk.Frame(self)
        self.frame_days.pack(pady=(0, 10))

    def init_needed_vars(self):
        self.month_names = ('', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
        self.day_names = ('Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb')

        # Inicia en 2026
        current_year = int(time.strftime("%Y"))
        self.year = str(max(current_year, 2026))
        self.month = 'Marzo'
        self.buttons = {}

        # Calendario inicia día domingo
        calendar.setfirstweekday(6)

    def init_month_year_labels(self):
        self.year_str_var = tk.StringVar()
        self.month_str_var = tk.StringVar()
        self.year_str_var.set(self.year)
        self.month_str_var.set(self.month)
        self.month_lbl = tk.Label(self.frame1, textvariable=self.month_str_var,
                                  width=14, font=('Arial', 12, 'bold'),
                                  bg="#D8BFD8", relief="raised", borderwidth=2)
        self.month_lbl.grid(row=0, column=1, padx=8, pady=(5, 2))

        self.year_lbl = tk.Label(self.frame1, textvariable=self.year_str_var,
                                 width=6, font=('Arial', 12, 'bold'),
                                 bg="#E6E6FA", relief="raised", borderwidth=2)
        self.year_lbl.grid(row=1, column=1, padx=8, pady=(2, 5))

    def init_buttons(self):
        # Botones de MES
        self.left_mon = tk.Button(self.frame1, text="◀", command=self.prev_month,
                                  bg="#E6E6FA", activebackground="#D4D4F8", activeforeground="#4B0082",
                                  relief="raised", borderwidth=3, font=('Arial', 9, 'bold'))
        self.left_mon.grid(row=0, column=0, padx=4, pady=(5, 2))

        self.right_mon = tk.Button(self.frame1, text="▶", command=self.next_month,
                                   bg="#E6E6FA", activebackground="#D4D4F8", activeforeground="#4B0082",
                                   relief="raised", borderwidth=3, font=('Arial', 9, 'bold'))
        self.right_mon.grid(row=0, column=2, padx=4, pady=(5, 2))

        # Botones de AÑO
        self.left_yr = tk.Button(self.frame1, text="◀", command=self.prev_year,
                                 bg="#D8BFD8", activebackground="#C8A8C8", activeforeground="#4B0082",
                                 relief="raised", borderwidth=3, font=('Arial', 9, 'bold'))
        self.left_yr.grid(row=1, column=0, padx=4, pady=(2, 5))

        self.right_yr = tk.Button(self.frame1, text="▶", command=self.next_year,
                                  bg="#D8BFD8", activebackground="#C8A8C8", activeforeground="#4B0082",
                                  relief="raised", borderwidth=3, font=('Arial', 9, 'bold'))
        self.right_yr.grid(row=1, column=2, padx=4, pady=(2, 5))

    def space_between_widgets(self):
        pass

    # Navegación de año con límites 2026-2036
    def prev_year(self):
        year = int(self.year_str_var.get()) - 1
        if year < 2026:
            messagebox.showinfo("Límite", "El año mínimo disponible es 2026")
            return
        self.year_str_var.set(str(year))
        self._update_year_buttons(year)
        self.make_calendar()

    def next_year(self):
        year = int(self.year_str_var.get()) + 1
        if year > 2036:
            messagebox.showinfo("Límite", "El año máximo disponible es 2036")
            return
        self.year_str_var.set(str(year))
        self._update_year_buttons(year)
        self.make_calendar()

    def _update_year_buttons(self, year):
        """Deshabilita los botones al alcanzar los límites del rango."""
        self.left_yr.config(state=tk.DISABLED if year <= 2026 else tk.NORMAL)
        self.right_yr.config(state=tk.DISABLED if year >= 2036 else tk.NORMAL)


    def prev_month(self):
        index = self.month_names.index(self.month_str_var.get())
        if index == 1:
            self.month_str_var.set(self.month_names[12])
        else:
            self.month_str_var.set(self.month_names[index - 1])
        self.make_calendar()

    def next_month(self):
        index = self.month_names.index(self.month_str_var.get())
        if index == 12:
            self.month_str_var.set(self.month_names[1])
        else:
            self.month_str_var.set(self.month_names[index + 1])
        self.make_calendar()

    def fill_days(self):
        for col, day in enumerate(self.day_names):
            lbl = tk.Label(self.frame_days, text=day, font=('Arial', 10, 'bold'),
                           width=4, bg="#DDA0DD", fg="white", relief="raised")
            lbl.grid(row=0, column=col, padx=1, pady=3)

    def make_calendar(self):
        for btn in self.buttons.values():
            btn.destroy()
        self.buttons.clear()

        year = int(self.year_str_var.get())
        month = self.month_names.index(self.month_str_var.get())

        self.m_cal = calendar.monthcalendar(year, month)

        for row_idx, week in enumerate(self.m_cal, 1):
            for col_idx, day in enumerate(week):
                if day == 0:
                    continue
                btn = tk.Button(self.frame_days, text=str(day), width=4, height=2,
                                bg="#F8F8FF", activebackground="#E6E6FA", activeforeground="#4B0082",
                                relief="raised", borderwidth=2, font=('Arial', 10, 'bold'))
                btn.grid(row=row_idx, column=col_idx, padx=1, pady=1, sticky='nsew')
                btn.bind('<Button-1>', lambda e, d=day: self.get_date(d))
                self.buttons[day] = btn

        # Refrescar estado de botones de año al redibujar
        self._update_year_buttons(year)

    def get_date(self, day):
        year = self.year_str_var.get()
        month_full = self.month_str_var.get()
        month_abbr = month_full[:3].title()
        self.full_date = f"{day:02d}/{month_abbr}/{year}"
        try:
            self.widget.delete(0, tk.END)
            self.widget.insert(0, self.full_date)
        except AttributeError:
            pass
        self.destroy()


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal - Tkinter")
        self.root.geometry("900x600")
        self.root.minsize(700, 500)

        frame_superior = ttk.LabelFrame(root, text="Eventos Programados")
        frame_superior.pack(fill=tk.BOTH, expand=False, padx=10, pady=(10, 5))

        columns = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(frame_superior, columns=columns, show="headings", height=8)
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.column("Fecha", width=120, anchor='center')
        self.tree.column("Hora", width=100, anchor='center')
        self.tree.column("Descripción", width=500)

        v_scrollbar = ttk.Scrollbar(frame_superior, orient=tk.VERTICAL, command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(frame_superior, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.frame_entrada = ttk.LabelFrame(root, text="Agregar Nuevo Evento")
        self.frame_entrada.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=8)
        self.entry_fecha = ttk.Entry(self.frame_entrada, width=20, font=('Arial', 10))
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=8, sticky=tk.W)
        self.btn_fecha = tk.Button(self.frame_entrada, text="📅 Seleccionar",
                                   command=lambda: DatePicker(self.entry_fecha),
                                   bg="#E6E6FA", activebackground="#D4D4F8", activeforeground="#4B0082",
                                   relief="raised", borderwidth=4, font=('Arial', 10, 'bold'))
        self.btn_fecha.grid(row=0, column=2, padx=5)

        ttk.Label(self.frame_entrada, text="Hora (HH:MM):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=8)
        self.entry_hora = ttk.Entry(self.frame_entrada, width=20, font=('Arial', 10))
        self.entry_hora.grid(row=1, column=1, padx=5, pady=8, sticky=tk.W)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0, sticky=tk.W + tk.N, padx=5, pady=8)
        self.entry_desc = ttk.Entry(self.frame_entrada, width=60, font=('Arial', 10))
        self.entry_desc.grid(row=2, column=1, columnspan=2, sticky=tk.W + tk.E, padx=5, pady=8)

        self.frame_entrada.columnconfigure(1, weight=1)

        frame_botones = tk.Frame(root, bg="#F8F8FF")
        frame_botones.pack(fill=tk.X, padx=10, pady=(5, 10))

        self.btn_agregar = tk.Button(frame_botones, text="➕ Agregar Evento", command=self.agregar_evento,
                                     bg="#DDA0DD", activebackground="#C71585", activeforeground="white",
                                     relief="raised", borderwidth=5, font=('Arial', 11, 'bold'))
        self.btn_agregar.pack(side=tk.LEFT, padx=(0, 15))

        self.btn_eliminar = tk.Button(frame_botones, text="🗑️ Eliminar Seleccionado", command=self.eliminar_evento,
                                      bg="#D8BFD8", activebackground="#9370DB", activeforeground="white",
                                      relief="raised", borderwidth=5, font=('Arial', 11, 'bold'))
        self.btn_eliminar.pack(side=tk.LEFT, padx=(0, 15))

        self.btn_salir = tk.Button(frame_botones, text="❌ Salir", command=root.quit,
                                   bg="#E6E6FA", activebackground="#BA55D3", activeforeground="white",
                                   relief="raised", borderwidth=5, font=('Arial', 11, 'bold'))
        self.btn_salir.pack(side=tk.RIGHT)

        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)

    def agregar_evento(self):
        fecha = self.entry_fecha.get().strip()
        hora = self.entry_hora.get().strip()
        desc = self.entry_desc.get().strip()
        if not (fecha and hora and desc):
            messagebox.showwarning("¡Advertencia!", "Complete todos los campos")
            return
        self.tree.insert("", tk.END, values=(fecha, hora, desc))
        self.limpiar_campos()
        messagebox.showinfo("¡Éxito!", "Evento agregado correctamente")

    def eliminar_evento(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("¡Advertencia!", "Seleccione un evento de la lista")
            return
        if messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de eliminar el evento seleccionado?"):
            self.tree.delete(selected[0])
            messagebox.showinfo("¡Éxito!", "Evento eliminado")

    def on_tree_select(self, event):
        pass

    def limpiar_campos(self):
        self.entry_fecha.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()