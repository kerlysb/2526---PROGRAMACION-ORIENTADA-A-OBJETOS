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

