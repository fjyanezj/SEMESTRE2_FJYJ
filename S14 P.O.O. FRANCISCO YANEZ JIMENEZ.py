import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Frame para la entrada de datos
        frame_entrada = tk.Frame(self.root)
        frame_entrada.pack(pady=10)

        # Etiquetas y campos de entrada
        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5)
        self.fecha_entry = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_entry.grid(row=0, column=1, padx=5)

        tk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5)
        self.hora_entry = tk.Entry(frame_entrada, width=10)
        self.hora_entry.grid(row=0, column=3, padx=5)

        tk.Label(frame_entrada, text="Descripción:").grid(row=0, column=4, padx=5)
        self.descripcion_entry = tk.Entry(frame_entrada, width=20)
        self.descripcion_entry.grid(row=0, column=5, padx=5)

        # Botones de acción
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=5)

        agregar_btn = tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento)
        agregar_btn.pack(side=tk.LEFT, padx=5)

        eliminar_btn = tk.Button(frame_botones, text="Eliminar Evento", command=self.eliminar_evento)
        eliminar_btn.pack(side=tk.LEFT, padx=5)

        salir_btn = tk.Button(frame_botones, text="Salir", command=root.quit)
        salir_btn.pack(side=tk.LEFT, padx=5)

        # Vista de eventos
        self.tree = ttk.Treeview(self.root, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.limpiar_campos()

    def eliminar_evento(self):
        try:
            item_seleccionado = self.tree.selection()[0]
            confirmar = messagebox.askyesno("Confirmar", "¿Desea eliminar el evento seleccionado?")
            if confirmar:
                self.tree.delete(item_seleccionado)
        except IndexError:
            messagebox.showwarning("Advertencia", "No hay ningún evento seleccionado.")

    def limpiar_campos(self):
        self.fecha_entry.set_date("")
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()