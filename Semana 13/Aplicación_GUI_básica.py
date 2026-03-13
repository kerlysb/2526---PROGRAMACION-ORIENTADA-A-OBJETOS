import tkinter as tk
from tkinter import ttk, messagebox

"""
Descripción de la Aplicación

Esta aplicación es un Registro de Contactos desarrollado con Python y Tkinter 
que permite a los usuarios almacenar y visualizar información de contactos de 
forma intuitiva. 

La interfaz incluye campos de texto para ingresar nombre, número de teléfono y 
correo electrónico, un botón "Agregar" para insertar los datos en una tabla, 
un botón "Limpiar Todo" que borra toda la información ingresada y la tabla, y 
un botón "Salir" para cerrar la aplicación. Utiliza ttk.Treeview para mostrar 
los contactos en formato tabular con columnas organizadas, respondiendo a los 
eventos de clic del usuario de manera eficiente.
"""

# Ventana principal
ventana = tk.Tk()
ventana.title("Registro de Contactos")
ventana.geometry("700x650")
ventana.resizable(True, True)


# Función para agregar contacto a la tabla
def agregar_contacto():
    nombre = entry_nombre.get().strip()
    telefono = entry_telefono.get().strip()
    correo = entry_correo.get().strip()

    if nombre and telefono and correo: #Condición para verificar que no estén los campos vacíos
        tabla.insert('', tk.END, values=(nombre, telefono, correo))
        limpiar_campos()
        messagebox.showinfo("Éxito", "¡Contacto agregado!")
    else:
        messagebox.showwarning("Error", "¡Llena todos los campos!")

# Función para limpiar y salir
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_correo.delete(0, tk.END)


def limpiar_todo():
    limpiar_campos()
    for item in tabla.get_children():
        tabla.delete(item)
    messagebox.showinfo("¡Listo!", "¡Tabla y campos limpiados!")


def salir():
    if messagebox.askyesno("Salir", "¿Quieres salir de la aplicación?"):
        ventana.quit()


# Etiquetas y Entradas
frame_form = tk.LabelFrame(ventana, text="Nuevo Contacto", font=("Arial", 11, "bold"))
frame_form.pack(pady=10, padx=10, fill="x")

tk.Label(frame_form, text="Nombre:", font=("Arial", 10)).pack(anchor="w", padx=10, pady=5)
entry_nombre = tk.Entry(frame_form, width=40, font=("Arial", 10))
entry_nombre.pack(padx=10, pady=2)

tk.Label(frame_form, text="Teléfono:", font=("Arial", 10)).pack(anchor="w", padx=10, pady=5)
entry_telefono = tk.Entry(frame_form, width=40, font=("Arial", 10))
entry_telefono.pack(padx=10, pady=2)

tk.Label(frame_form, text="Correo:", font=("Arial", 10)).pack(anchor="w", padx=10, pady=5)
entry_correo = tk.Entry(frame_form, width=40, font=("Arial", 10))
entry_correo.pack(padx=10, pady=2)

# Configuración de botón agregar
btn_agregar = tk.Button(ventana,
                        text="Agregar",
                        command=agregar_contacto,
                        bg="#32CD32",
                        activebackground="#228B22",
                        activeforeground="#F50743",
                        relief="raised",
                        borderwidth=5,
                        width=12,
                        font=("Arial", 10, "bold"))
btn_agregar.pack(pady=15)

# Tabla exterior
frame_tabla = tk.LabelFrame(ventana, text="Lista de Contactos", font=("Arial", 11, "bold"))
frame_tabla.pack(pady=10, padx=10, fill="both", expand=False)

# Tablas de contenido
scrollbar = ttk.Scrollbar(frame_tabla)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tabla = ttk.Treeview(frame_tabla, columns=('Nombre', 'Teléfono', 'Correo'),
                     show='headings', height=10, yscrollcommand=scrollbar.set)
scrollbar.config(command=tabla.yview)

tabla.heading('Nombre', text='Nombre')
tabla.heading('Teléfono', text='Teléfono')
tabla.heading('Correo', text='Correo')
tabla.column('Nombre', width=160)
tabla.column('Teléfono', width=130)
tabla.column('Correo', width=160)
tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configuración de botones limpiar y salir
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=20)

btn_limpiar = tk.Button(frame_botones,
                        text="Limpiar Todo",
                        command=limpiar_todo,
                        bg="#FF8C00",
                        activebackground="#FF4500",
                        activeforeground="#F50743",
                        relief="raised",
                        borderwidth=5,
                        width=14,
                        height=2,
                        font=("Arial", 11, "bold"))
btn_limpiar.pack(side=tk.LEFT, padx=20)

btn_salir = tk.Button(frame_botones,
                      text="Salir",
                      command=salir,
                      bg="#DC143C",
                      activebackground="#B22222",
                      activeforeground="#F50743",
                      relief="raised",
                      borderwidth=5,
                      width=14,
                      height=2,
                      font=("Arial", 11, "bold"))
btn_salir.pack(side=tk.LEFT, padx=20)

# Iniciar aplicación
ventana.mainloop()

