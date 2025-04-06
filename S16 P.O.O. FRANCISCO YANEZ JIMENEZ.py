import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Entrada de tarea
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=10)
        self.entry.focus()

        # Botones
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        self.add_button = tk.Button(button_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(button_frame, text="Marcar Completada", command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        # Diccionario para estado de tareas
        self.tasks = {}

        # Atajos de teclado globales (funcionan sin importar el foco)
        self.root.bind_all("<Return>", self.handle_enter)
        self.root.bind_all("<c>", self.handle_complete)
        self.root.bind_all("<C>", self.handle_complete)
        self.root.bind_all("<d>", self.handle_delete)
        self.root.bind_all("<D>", self.handle_delete)
        self.root.bind_all("<Delete>", self.handle_delete)
        self.root.bind_all("<Escape>", lambda event: self.root.quit())

    # --- Atajo Handlers separados ---
    def handle_enter(self, event):
        if self.entry.focus_get() == self.entry:
            self.add_task()

    def handle_complete(self, event):
        self.complete_task()

    def handle_delete(self, event):
        self.delete_task()

    # --- Funciones principales ---
    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text == "":
            messagebox.showwarning("Aviso", "No puedes añadir una tarea vacía.")
            return

        self.task_listbox.insert(tk.END, task_text)
        self.tasks[task_text] = False
        self.entry.delete(0, tk.END)

    def complete_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showinfo("Aviso", "Selecciona una tarea para marcar como completada.")
            return

        index = selected[0]
        task_text = self.task_listbox.get(index)

        if task_text.startswith("[✔]"):
            messagebox.showinfo("Info", "La tarea ya está completada.")
            return

        # Marcar como completada
        self.tasks[task_text] = True
        self.task_listbox.delete(index)
        self.task_listbox.insert(index, f"[✔] {task_text}")
        self.task_listbox.itemconfig(index, fg="gray")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showinfo("Aviso", "Selecciona una tarea para eliminar.")
            return

        index = selected[0]
        task_text = self.task_listbox.get(index)

        task_key = task_text.replace("[✔] ", "") if task_text.startswith("[✔]") else task_text

        if task_key in self.tasks:
            del self.tasks[task_key]

        self.task_listbox.delete(index)

# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
