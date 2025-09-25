import tkinter as tk  # Importo la biblioteca Tkinter para crear la interfaz gráfica.
from tkinter import messagebox  # Importo el módulo messagebox para mostrar mensajes de advertencia.

class TaskManager:  # Defino la clase TaskManager que manejará la lógica de la aplicación.
    def __init__(self, root):  # Inicializo la clase con el parámetro root que representa la ventana principal.
        self.root = root  # Asigno la ventana principal a un atributo de la clase.
        self.root.title("Gestor de Tareas")  # Establezco el título de la ventana.

        self.tasks = []  # Inicializo una lista vacía para almacenar las tareas.

        # Creo un campo de entrada para que el usuario escriba nuevas tareas.
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)  # Coloco el campo de entrada en la ventana con un margen vertical.
        self.task_entry.bind('<Return>', self.add_task)  # Asigno la función add_task al evento de pulsar Enter.

        # Creo un botón para añadir tareas.
        self.add_task_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)  # Coloco el botón en la ventana con un margen vertical.

        # Creo un Listbox para mostrar las tareas actuales.
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)  # Coloco el Listbox en la ventana con un margen vertical.

        # Creo un botón para marcar tareas como completadas.
        self.complete_task_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)  # Coloco el botón en la ventana con un margen vertical.

        # Creo un botón para eliminar tareas.
        self.delete_task_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)  # Coloco el botón en la ventana con un margen vertical.

    def add_task(self, event=None):  # Defino la función para añadir tareas, permitiendo un evento opcional.
        task = self.task_entry.get()  # Obtengo el texto del campo de entrada.
        if task:  # Verifico si el campo de entrada no está vacío.
            self.tasks.append(task)  # Agrego la tarea a la lista de tareas.
            self.update_task_list()  # Actualizo la lista mostrada en el Listbox.
            self.task_entry.delete(0, tk.END)  # Limpio el campo de entrada.
        else:  # Si el campo de entrada está vacío.
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")  # Muestro un mensaje de advertencia.

    def complete_task(self):  # Defino la función para marcar tareas como completadas.
        try:
            selected_task_index = self.task_listbox.curselection()[0]  # Obtengo el índice de la tarea seleccionada.
            completed_task = self.tasks[selected_task_index]  # Obtengo la tarea seleccionada.
            self.tasks[selected_task_index] = f"{completed_task} (Completada)"  # Actualizo la tarea para marcarla como completada.
            self.update_task_list()  # Actualizo la lista mostrada en el Listbox.
        except IndexError:  # Si no hay ninguna tarea seleccionada.
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")  # Muestro un mensaje de advertencia.

    def delete_task(self):  # Defino la función para eliminar tareas.
        try:
            selected_task_index = self.task_listbox.curselection()[0]  # Obtengo el índice de la tarea seleccionada.
            del self.tasks[selected_task_index]  # Elimino la tarea de la lista.
            self.update_task_list()  # Actualizo la lista mostrada en el Listbox.
        except IndexError:  # Si no hay ninguna tarea seleccionada.
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")  # Muestro un mensaje de advertencia.

    def update_task_list(self):  # Defino la función para actualizar el Listbox con las tareas actuales.
        self.task_listbox.delete(0, tk.END)  # Limpio el Listbox.
        for task in self.tasks:  # Itero sobre la lista de tareas.
            self.task_listbox.insert(tk.END, task)  # Inserto cada tarea en el Listbox.

if __name__ == "__main__":  # Verifico si este archivo se está ejecutando como programa principal.
    root = tk.Tk()  # Creo la ventana principal.
    task_manager = TaskManager(root)  # Instancio la clase TaskManager.
    root.mainloop()  # Inicio el bucle principal de la interfaz gráfica.