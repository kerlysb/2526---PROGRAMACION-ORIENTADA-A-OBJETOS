import tkinter as tk
from tkinter import ttk, messagebox

"""
Descripción de la Aplicación

Esta aplicación es un Registro de Contactos desarrollado con Python y Tkinter 
que permite a los usuarios almacenar y visualizar información de contactos de 
forma intuitiva. 

La interfaz incluye campos de texto para ingresar nombre, número de teléfono y 
correo electrónico, un botón "Agregar" para insertar los datos en una tabla, y 
un botón "Limpiar" que borra toda la información ingresada y la tabla. Utiliza 
ttk.Treeview para mostrar los contactos en formato tabular con columnas 
organizadas, respondiendo a los eventos de clic del usuario de manera eficiente.
"""

# Ventana principal
ventana = tk.Tk()
ventana.title("Registro de Contactos")
ventana.geometry("650x550")

# Función para agregar contacto a la tabla
def agregar_contacto():
    nombre = entry_nombre.get().strip()
    telefono = entry_telefono.get().strip()
    correo = entry_correo.get().strip()
    if nombre and telefono and correo: # Verifica que no estén vacíos
        tabla.insert('', tk.END, values=(nombre, telefono, correo))
        limpiar_campos()
    else:
        messagebox.showwarning("Error", "¡Llena todos los campos!")

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_correo.delete(0, tk.END)

def limpiar_todo():
    limpiar_campos()
    for item in tabla.get_children():
        tabla.delete(item)
    messagebox.showinfo("¡Listo!", "Tabla y campos limpiados")

def salir():
    if messagebox.askyesno("Salir", "¿Quieres salir?"):
        ventana.quit()

# Labels y Entries
tk.Label(ventana, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.pack(pady=2)

tk.Label(ventana, text="Teléfono:").pack(pady=5)
entry_telefono = tk.Entry(ventana, width=40)
entry_telefono.pack(pady=2)

tk.Label(ventana, text="Correo:").pack(pady=5)
entry_correo = tk.Entry(ventana, width=40)
entry_correo.pack(pady=2)

btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_contacto, bg="lightgreen")
btn_agregar.pack(pady=10)

# Scrollbar para la tabla
scrollbar = ttk.Scrollbar(ventana)
tabla = ttk.Treeview(ventana, columns=('Nombre', 'Teléfono', 'Correo'),
                     show='headings', height=8, yscrollcommand=scrollbar.set)
scrollbar.config(command=tabla.yview)

# Configurar columnas
tabla.heading('Nombre', text='Nombre')
tabla.heading('Teléfono', text='Teléfono')
tabla.heading('Correo', text='Correo')
tabla.column('Nombre', width=150)
tabla.column('Teléfono', width=120)
tabla.column('Correo', width=150)

# Empaquetar tabla y scrollbar lado a lado
tabla.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)

# Frame para botones (¡AHORA SÍ SE VEN!)
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_limpiar = tk.Button(frame_botones, text="Limpiar Todo",
                        command=limpiar_todo, bg="orange", width=12)
btn_limpiar.pack(side=tk.LEFT, padx=10)

btn_salir = tk.Button(frame_botones, text="Salir",
                      command=salir, bg="red", width=12)
btn_salir.pack(side=tk.LEFT, padx=10)

ventana.mainloop()
