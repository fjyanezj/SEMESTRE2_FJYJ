import tkinter as tk
from tkinter import messagebox

# Función para añadir tarea
def añadir_tarea():
    tarea = entrada_tarea.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, ingresa una tarea.")

# Función para marcar tarea como completada
def marcar_completada():
    try:
        tarea_seleccionada = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(tarea_seleccionada)
        lista_tareas.delete(tarea_seleccionada)
        lista_tareas.insert(tarea_seleccionada, tarea + " - Completada")
    except IndexError:
        messagebox.showwarning("Selección requerida", "Por favor, selecciona una tarea para marcar como completada.")

# Función para eliminar tarea
def eliminar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()[0]
        lista_tareas.delete(tarea_seleccionada)
    except IndexError:
        messagebox.showwarning("Selección requerida", "Por favor, selecciona una tarea para eliminar.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Tareas")

# Crear los componentes de la interfaz
entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=10)

boton_añadir = tk.Button(ventana, text="Añadir Tarea", width=20, command=añadir_tarea)
boton_añadir.pack(pady=5)

boton_completada = tk.Button(ventana, text="Marcar como Completada", width=20, command=marcar_completada)
boton_completada.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", width=20, command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Crear un Listbox para mostrar las tareas
lista_tareas = tk.Listbox(ventana, height=10, width=50)
lista_tareas.pack(pady=10)

# Funcionalidad de añadir tarea con tecla Enter
ventana.bind('<Return>', lambda event: añadir_tarea())

# Ejecutar la ventana principal
ventana.mainloop()
