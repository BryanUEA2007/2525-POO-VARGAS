# Importo tkinter como tk para crear la interfaz gráfica
import tkinter as tk
# Importo ttk para usar widgets con mejor apariencia y messagebox para mostrar mensajes al usuario
from tkinter import ttk, messagebox
# Importo DateEntry de tkcalendar que me permitirá implementar un selector de fechas
from tkcalendar import DateEntry
# Importo datetime para trabajar con fechas y horas
from datetime import datetime
# Defino la clase principal de mi aplicación
class CalendarioApp:
    # Inicializo con el metodo constructor
    def __init__(self, root):
        # Guardo la ventana raíz en un atributo de la clase
        self.root = root
        # Establezco el título de mi ventana principal
        self.root.title("Calendario de Eventos")
        # Configuro el tamaño inicial de mi ventana
        self.root.geometry("700x500")
        # Permito que mi ventana pueda cambiar de tamaño
        self.root.resizable(True, True)

        # Creo un frame para mostrar la lista de eventos
        self.frame_eventos = ttk.Frame(root, padding="10")
        # Creo un frame para los campos donde el usuario ingresará datos
        self.frame_entrada = ttk.Frame(root, padding="10")
        # Creo un frame para los botones de acción
        self.frame_acciones = ttk.Frame(root, padding="10")

        # Coloco el frame de eventos en la parte superior
        self.frame_eventos.pack(fill=tk.BOTH, expand=True)
        # Coloco el frame de entrada debajo con un poco de espacio alrededor
        self.frame_entrada.pack(fill=tk.X, padx=10, pady=5)
        # Coloco el frame de acciones en la parte inferior
        self.frame_acciones.pack(fill=tk.X, padx=10, pady=5)

        # Llamo al metodo que configurará el TreeView para mostrar los eventos
        self.configurar_treeview()

        # Llamo al metodo que configurará los campos para ingresar datos
        self.configurar_campos_entrada()

        # Llamo al metodo que configurará los botones de acción
        self.configurar_botones()

    # Defino el metodo para configurar el TreeView
    def configurar_treeview(self):
        # Creo un frame específico para el TreeView y su barra de desplazamiento
        frame_treeview = ttk.Frame(self.frame_eventos)

        frame_treeview.pack(fill=tk.BOTH, expand=True)

        # Creo una barra de desplazamiento vertical
        scrollbar = ttk.Scrollbar(frame_treeview)
        # La coloco en el lado derecho del frame
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Defino las columnas que tendrá mi TreeView
        columnas = ("fecha", "hora", "descripcion")
        # Creo el TreeView con las columnas definidas y lo conecto con la barra de desplazamiento
        self.treeview = ttk.Treeview(frame_treeview, columns=columnas, show="headings", yscrollcommand=scrollbar.set)

        # Configuro el encabezado de la columna fecha
        self.treeview.heading("fecha", text="Fecha")
        # Configuro el encabezado de la columna hora
        self.treeview.heading("hora", text="Hora")
        # Configuro el encabezado de la columna descripción
        self.treeview.heading("descripcion", text="Descripción")

        # Establezco el ancho de la columna fecha
        self.treeview.column("fecha", width=100)
        # Establezco el ancho de la columna hora
        self.treeview.column("hora", width=100)
        # Establezco el ancho de la columna descripción, más ancha para mostrar más texto
        self.treeview.column("descripcion", width=400)


        self.treeview.pack(fill=tk.BOTH, expand=True)

        # Conecto la barra de desplazamiento con el metodo yview del TreeView
        scrollbar.config(command=self.treeview.yview)

        # Creo una etiqueta como título para la lista de eventos
        lbl_eventos = ttk.Label(self.frame_eventos, text="Lista de Eventos", font=("Arial", 12, "bold"))
        # Coloco la etiqueta anclada al oeste (izquierda) con un poco de espacio debajo
        lbl_eventos.pack(anchor=tk.W, pady=(0, 5))

    # Defino el metodo para configurar los campos de entrada
    def configurar_campos_entrada(self):
        # Creo un sub-frame para organizar los campos en una sola línea
        frame_campos = ttk.Frame(self.frame_entrada)

        frame_campos.pack(fill=tk.X)

        # Creo una etiqueta para el campo de fecha
        lbl_fecha = ttk.Label(frame_campos, text="Fecha:", width=10)
        # La coloco en la primera fila, primera columna de mi grid
        lbl_fecha.grid(row=0, column=0, padx=5, pady=5)

        # Creo el selector de fechas con un fondo azul oscuro y texto blanco
        self.date_picker = DateEntry(frame_campos, width=12, background='darkblue',
                                     foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        # Lo coloco a la derecha de su etiqueta
        self.date_picker.grid(row=0, column=1, padx=5, pady=5)

        # Creo una etiqueta para el campo de hora
        lbl_hora = ttk.Label(frame_campos, text="Hora:", width=10)
        # La coloco en la primera fila, tercera columna
        lbl_hora.grid(row=0, column=2, padx=5, pady=5)

        # Creo un campo de entrada para la hora
        self.entry_hora = ttk.Entry(frame_campos, width=10)
        # Lo coloco a la derecha de su etiqueta
        self.entry_hora.grid(row=0, column=3, padx=5, pady=5)
        # Inserto un texto predeterminado como ayuda para el usuario
        self.entry_hora.insert(0, "HH:MM")

        # Creo una etiqueta para el campo de descripción
        lbl_descripcion = ttk.Label(frame_campos, text="Descripción:", width=10)
        # La coloco en la primera fila, quinta columna
        lbl_descripcion.grid(row=0, column=4, padx=5, pady=5)

        # Creo un campo de entrada para la descripción, más ancho para permitir textos largos
        self.entry_descripcion = ttk.Entry(frame_campos, width=30)
        # Lo coloco a la derecha de su etiqueta
        self.entry_descripcion.grid(row=0, column=5, padx=5, pady=5)

    # Defino el metodo para configurar los botones de acción
    def configurar_botones(self):
        # Creo un sub-frame para organizar los botones
        frame_botones = ttk.Frame(self.frame_acciones)
        # Lo coloco en el centro
        frame_botones.pack()

        # Creo el botón para agregar eventos y lo vinculo con su función correspondiente
        self.btn_agregar = ttk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento)
        # Lo coloco en la primera posición
        self.btn_agregar.grid(row=0, column=0, padx=10, pady=5)

        # Creo el botón para eliminar eventos y lo vinculo con su función
        self.btn_eliminar = ttk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        # Lo coloco en la segunda posición
        self.btn_eliminar.grid(row=0, column=1, padx=10, pady=5)

        # Creo el botón para salir de la aplicación y lo vinculo con la función destroy de la ventana raíz
        self.btn_salir = ttk.Button(frame_botones, text="Salir", command=self.root.destroy)
        # Lo coloco en la tercera posición
        self.btn_salir.grid(row=0, column=2, padx=10, pady=5)

    # Defino el metodo para agregar un evento a la lista
    def agregar_evento(self):
        # Obtengo la fecha seleccionada y la convierto a formato dd/mm/yyyy
        fecha = self.date_picker.get_date().strftime('%d/%m/%Y')
        # Obtengo la hora ingresada
        hora = self.entry_hora.get()
        # Obtengo la descripción ingresada
        descripcion = self.entry_descripcion.get()

        # Verifico que todos los campos tengan información válida
        if not hora or hora == "HH:MM" or not descripcion:
            # Si falta algún dato, muestro un mensaje de error
            messagebox.showerror("Error", "Por favor, complete todos los campos")
            # Salgo de la función sin agregar nada
            return

        # Verifico que la hora tenga el formato correcto
        try:
            # Intento convertir la hora a un objeto datetime
            datetime.strptime(hora, '%H:%M')
        except ValueError:
            # Si hay un error, muestro un mensaje al usuario
            messagebox.showerror("Error", "El formato de hora debe ser HH:MM")
            # Salgo de la función sin agregar nada
            return


        self.treeview.insert('', tk.END, values=(fecha, hora, descripcion))

        # Limpio el campo de hora
        self.entry_hora.delete(0, tk.END)
        # Reinserto el texto de ayuda
        self.entry_hora.insert(0, "HH:MM")
        # Limpio el campo de descripción
        self.entry_descripcion.delete(0, tk.END)

        # Muestro un mensaje de confirmación al usuario
        messagebox.showinfo("Éxito", "Evento agregado correctamente")

    # Defino el metodo para eliminar un evento seleccionado
    def eliminar_evento(self):
        # Obtengo el elemento seleccionado en el TreeView
        seleccionado = self.treeview.selection()

        # Verifico si hay algún elemento seleccionado
        if not seleccionado:
            # Si no hay nada seleccionado, muestro una advertencia
            messagebox.showwarning("Advertencia", "Por favor, seleccione un evento para eliminar")
            # Salgo de la función sin eliminar nada
            return

        # Pido confirmación antes de eliminar
        confirmar = messagebox.askyesno("Confirmar eliminación", "¿Está seguro que desea eliminar este evento?")

        # Si el usuario confirma la eliminación
        if confirmar:
            # Elimino el elemento seleccionado del TreeView
            self.treeview.delete(seleccionado)
            # Muestro un mensaje de confirmación
            messagebox.showinfo("Éxito", "Evento eliminado correctamente")


# Si este archivo se ejecuta directamente (no como módulo)
if __name__ == "__main__":
    # Creo la ventana principal
    root = tk.Tk()
    # Inicializo mi aplicación con la ventana principal
    app = CalendarioApp(root)
    # Inicio el bucle principal de eventos
    root.mainloop()

