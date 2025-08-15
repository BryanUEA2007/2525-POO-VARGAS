# Creo una clase llamada Producto p
class Producto:

    # Creo el metodo constructor para inicializar mis atributos
    def __init__(self, id, nombre, cantidad, precio):
        # Guardo el identificador único del producto.
        self.id = id
        # Guardo el nombre que me describe.
        self.nombre = nombre
        # Guardo cuántas unidades hay disponibles de mí.
        self.cantidad = cantidad
        # Guardo cuánto cuesta adquirir una unidad de mí.
        self.precio = precio

    # Creo un metodo para devolver mi id cuando lo necesiten.
    def get_id(self):
        return self.id

    # Creo un metodo para devolver mi nombre.
    def get_nombre(self):
        return self.nombre


    def get_cantidad(self):
        return self.cantidad

    # Creo un metodo para devolver el  precio.
    def get_precio(self):
        return self.precio

    # Creo un metodo para cambiar el nombre si es necesario.
    def set_nombre(self, nombre):
        self.nombre = nombre

    # Creo un metodo para actualizar la cantidad disponible .
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    # Creo un metodo para modificar el precio.
    def set_precio(self, precio):
        self.precio = precio

    # Creo un metodo especial para mostrar como texto
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:  # Estoy definiendo la clase Inventario para gestionar una colección de productos.
        def __init__(self):  # Al crear una instancia, inicializo la lista de productos.
            self.productos = []  # Aquí guardo todos los productos que se añadan al inventario.

        def añadir_producto(self, producto):  # Este metodo me permite añadir un nuevo producto.
            if any(p.get_id() == producto.get_id() for p in
                   self.productos):  # Verifico si ya existe un producto con el mismo ID.
                print(" Error: El ID ya existe.")  # Si el ID está repetido, muestro un mensaje de error.
            else:
                self.productos.append(producto)
                print(" Producto añadido correctamente.")  # Confirmo que se añadió correctamente.

        def eliminar_producto(self, id):  # Este metodo elimina un producto según su ID.
            for p in self.productos:  # Recorro todos los productos.
                if p.get_id() == id:
                    self.productos.remove(p)
                    print("🗑️ Producto eliminado.")  # Informo que fue eliminado.
                    return  # Salgo del metodo.
            print(" Producto no encontrado.")  # Si no lo encuentro, muestro un mensaje de error.

        def actualizar_producto(self, id, cantidad=None,
                                precio=None):  # Este metodo actualiza la cantidad o precio de un producto.
            for p in self.productos:  # Recorro todos los productos.
                if p.get_id() == id:
                    if cantidad is not None:  # Si se especificó una nueva cantidad...
                        p.set_cantidad(cantidad)  # ...la actualizo.
                    if precio is not None:  # Si se especificó un nuevo precio...
                        p.set_precio(precio)  # ...lo actualizo.
                    print(" Producto actualizado.")  # Confirmo que se actualizó.
                    return  # Salgo del metodo.
            print(" Producto no encontrado.")  # Si no lo encuentro, muestro un mensaje de error.

        def buscar_por_nombre(self, nombre):  # Este metodo busca productos por nombre.
            resultados = [p for p in self.productos if
                          nombre.lower() in p.get_nombre().lower()]  # Busco coincidencias ignorando mayúsculas/minúsculas.
            if resultados:
                for p in resultados:  # los recorro uno por uno
                    print(p)  # y los muestro.
            else:  # Si no hay coincidencias...
                print("No se encontraron productos con ese nombre.")  # informo que no se encontró nada.

        def mostrar_todos(self):  # Este metodo muestra todos los productos del inventario.
            if not self.productos:
                print(" Inventario vacío.")
            else:  # Si hay productos...
                for p in self.productos:
                    print(p)  # los imprimo.

def menu():  # Defino la función principal del menú para interactuar con el inventario.
    inventario = Inventario()  # Creo una instancia de la clase Inventario para comenzar a trabajar.

    while True:  # Inicio un bucle infinito para mostrar el menú hasta que el usuario decida salir.
        print("\n MENÚ DE INVENTARIO")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")  # Pido al usuario que seleccione una opción.

        if opcion == "1":
            try:  # Uso try para manejar posibles errores de entrada.
                id = input("ID: ")  # Solicito el ID del producto.
                nombre = input("Nombre: ")  # Solicito el nombre del producto.
                cantidad = int(input("Cantidad: "))  # Solicito la cantidad y la convierto a entero.
                precio = float(input("Precio: "))  # Solicito el precio y lo convierto a flotante.
                producto = Producto(id, nombre, cantidad, precio)  # Creo una instancia de Producto con los datos ingresados.
                inventario.añadir_producto(producto)  # Llamo al metodo para añadir el producto al inventario.
            except ValueError:  # Si hay un error al convertir cantidad o precio...
                print(" Entrada inválida.")  # ...muestro un mensaje de advertencia.

        elif opcion == "2":  # Si elige eliminar producto...
            id = input("ID del producto a eliminar: ")  # Solicito el ID del producto a eliminar.
            inventario.eliminar_producto(id)  # Llamo al metodo para eliminarlo.

        elif opcion == "3":  # Si elige actualizar producto...
            id = input("ID del producto a actualizar: ")  # Solicito el ID del producto.
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")  # Pido la nueva cantidad.
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")  # Pido el nuevo precio.
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)  # Llamo al metodo para actualizar el producto.

        elif opcion == "4":  # Si elige buscar producto por nombre...
            nombre = input("Nombre a buscar: ")  # Solicito el nombre a buscar.
            inventario.buscar_por_nombre(nombre)  # Llamo al metodo para buscar productos.

        elif opcion == "5":  # Si elige mostrar todos los productos...
            inventario.mostrar_todos()  # Llamo al metodo para mostrar el inventario completo.

        elif opcion == "6":  # Si elige salir...
            print(" ¡Hasta luego!")  # Muestro un mensaje de despedida.
            break  # Salgo del bucle y termino el programa.

        else:  # Si elige una opción no válida...

           print(" Opción inválida.")  # Muestro un mensaje de error.

if __name__ == "__main__":
    menu()