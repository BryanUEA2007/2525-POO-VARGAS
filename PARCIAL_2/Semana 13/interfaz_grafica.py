import tkinter as tk  # Importo el módulo tkinter con un alias corto para facilitar su uso
from tkinter import messagebox  # Importo el submódulo messagebox para poder mostrar alertas al usuario

# Crear la ventana principal
root = tk.Tk()  # Creo la ventana raíz de mi aplicación
root.title("Gestión de Productos")  # Le asigno un título descriptivo a mi ventana


frame_input = tk.Frame(root)  # Creo un marco para organizar los elementos de entrada
frame_input.pack(pady=10)  # Coloco el marco con un espacio vertical de 10 píxeles

# Etiquetas y campos de texto para el nombre y precio del producto
label_nombre = tk.Label(frame_input, text="Nombre del producto:")  # Creo una etiqueta para el nombre
label_nombre.pack(side=tk.LEFT, padx=5)  # La coloco a la izquierda con espacio horizontal
entry_nombre = tk.Entry(frame_input, width=20)  # Creo un campo de texto para escribir el nombre
entry_nombre.pack(side=tk.LEFT, padx=5)  # Lo coloco a la derecha de la etiqueta

label_precio = tk.Label(frame_input, text="Precio del producto:")  # Creo una etiqueta para el precio
label_precio.pack(side=tk.LEFT, padx=5)  # La coloco a la izquierda del campo de precio
entry_precio = tk.Entry(frame_input, width=10)  # Creo un campo de texto para escribir el precio
entry_precio.pack(side=tk.LEFT, padx=5)  # Lo coloco a la derecha de la etiqueta de precio

# Lista para mostrar los productos y precios
listbox = tk.Listbox(root, width=50, height=10)  # Creo una lista para mostrar los productos agregados
listbox.pack(pady=10)  # La coloco debajo de los campos de entrada con espacio vertical


# Funciones de los botones
def agregar_producto():  # Defino la función que se ejecutará al presionar el botón Agregar
    nombre = entry_nombre.get()
    precio = entry_precio.get()

    if nombre and precio:  # Verifico que ambos campos tengan contenido
        try:
            float(precio)  # Intento convertir el precio a número decimal para validarlo
            listbox.insert(tk.END, f"{nombre} - ${precio}")  # Inserto el producto al final de la lista
            entry_nombre.delete(0, tk.END)  # Limpio el campo de nombre para facilitar el siguiente ingreso
            entry_precio.delete(0, tk.END)  # Limpio el campo de precio para facilitar el siguiente ingreso
        except ValueError:  # Capturo el error si el precio no es un número válido
            messagebox.showerror("Error", "El precio debe ser un número válido.")  # Muestro un mensaje de error
    else:  # Si alguno de los campos está vacío
        messagebox.showwarning("Advertencia", "Ambos campos deben estar llenos.")  # Muestro una advertencia


def limpiar_lista():  # Defino la función que se ejecutará al presionar el botón Limpiar
    listbox.delete(0, tk.END)  # Elimino todos los elementos de la lista, desde el primero hasta el último


# Botones
frame_buttons = tk.Frame(root)  # Creo un marco para organizar los botones
frame_buttons.pack(pady=10)  # Lo coloco debajo de la lista con espacio vertical

btn_agregar = tk.Button(frame_buttons, text="Agregar", command=agregar_producto)  # Creo un botón para agregar productos
btn_agregar.pack(side=tk.LEFT, padx=5)  # Lo coloco a la izquierda con espacio horizontal

btn_limpiar = tk.Button(frame_buttons, text="Limpiar", command=limpiar_lista)  # Creo un botón para limpiar la lista
btn_limpiar.pack(side=tk.LEFT, padx=5)  # Lo coloco a la derecha del botón agregar

# Ejecutar la ventana principal
root.mainloop()  # Inicio el bucle principal de eventos para que la interfaz responda a las acciones del usuario