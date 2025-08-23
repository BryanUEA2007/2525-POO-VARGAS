import json  # Importa el módulo JSON para guardar y cargar datos en formato estructurado.
import os    # Importa el módulo OS para trabajar con rutas de archivos y el sistema operativo.


# Definimos la clase Producto que representa cada ítem del inventario.
class Producto:
    """Representa un producto con ID, nombre, cantidad y precio."""

    def __init__(self, id_producto, nombre, cantidad, precio):
        # Validamos que cantidad y precio no sean negativos.
        if cantidad < 0 or precio < 0:
            raise ValueError("La cantidad y el precio deben ser no negativos.")
        # Guardamos los atributos como privados.
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Propiedad para acceder al ID del producto.
    @property
    def id(self):
        return self._id

    # Propiedad para acceder al nombre del producto.
    @property
    def nombre(self):
        return self._nombre

    # Propiedad para acceder a la cantidad disponible.
    @property
    def cantidad(self):
        return self._cantidad

    # Propiedad para acceder al precio unitario.
    @property
    def precio(self):
        return self._precio

    # Metodo para cambiar el nombre del producto.
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # Metodo para actualizar la cantidad, validando que no sea negativa.
    def set_cantidad(self, nueva_cantidad):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self._cantidad = nueva_cantidad

    # Metodo para actualizar el precio, validando que no sea negativo.
    def set_precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = nuevo_precio

    # Convierte el producto en un diccionario para guardarlo en JSON.
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    # Representación textual del producto para impresión.
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# Clase Inventario que gestiona una colección de productos.
class Inventario:
    """Gestiona una colección de productos con persistencia en archivo."""

    def __init__(self, archivo="inventario_otro.json"):
        self.productos = []       # Lista que almacena los productos.
        self.archivo = archivo    # Nombre del archivo donde se guarda el inventario.
        self.cargar_archivo()     # Carga los datos del archivo al iniciar.

    # Guarda el inventario en un archivo JSON.
    def guardar_archivo(self):
        try:
            productos_dict = [p.to_dict() for p in self.productos]  # Convertimos cada producto a diccionario.
            with open(self.archivo, "w") as f:                      # Abrimos el archivo en modo escritura.
                json.dump(productos_dict, f, indent=4)              # Guardamos la lista en formato JSON.
            print(f" Cambios guardados en: {os.path.abspath(self.archivo)}")  # Confirmamos ruta del archivo.
        except Exception as e:
            print(f"Error al guardar: {e}")  # Mostramos cualquier error que ocurra.

    # Carga los productos desde el archivo JSON.
    def cargar_archivo(self):
        try:
            with open(self.archivo, "r") as f:         # Abrimos el archivo en modo lectura.
                datos = json.load(f)                   # Cargamos los datos JSON como lista de diccionarios.
                for d in datos:                        # Iteramos sobre cada diccionario.
                    producto = Producto(               # Creamos un objeto Producto con los datos.
                        d["id"], d["nombre"], int(d["cantidad"]), float(d["precio"])
                    )
                    self.productos.append(producto)    # Lo añadimos a la lista de productos.
            print(f" Inventario cargado: {len(self.productos)} productos.")  # Mostramos cuántos se cargaron.
        except FileNotFoundError:
            print(" Archivo no encontrado. Se creará uno nuevo al guardar.")  # Si no existe, se avisa.
        except json.JSONDecodeError:
            print("⚠ El archivo no tiene formato JSON válido.")  # Si el archivo está corrupto.
        except Exception as e:
            print(f" Error al cargar archivo: {e}")  # Otro tipo de error.

    # Añade un nuevo producto al inventario.
    def añadir_producto(self, producto):
        if any(p.id == producto.id for p in self.productos):  # Verifica si el ID ya existe.
            print(" Error: El ID ya existe.")
        else:
            self.productos.append(producto)  # Añade el producto.
            self.guardar_archivo()           # Guarda los cambios.
            print(" Producto añadido correctamente.")

    # Elimina un producto por su ID.
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.id == id_producto:
                self.productos.remove(p)  # Lo elimina de la lista.
                self.guardar_archivo()    # Guarda los cambios.
                print("🗑 Producto eliminado.")
                return
        print("⚠ Producto no encontrado.")

    # Actualiza la cantidad y/o precio de un producto.
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.id == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                self.guardar_archivo()
                print("🔄 Producto actualizado.")
                return
        print("⚠️ Producto no encontrado.")

    # Busca productos por nombre (parcial, sin importar mayúsculas).
    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            print("\n Resultados de búsqueda:")
            self.mostrar_tabla(resultados)
        else:
            print("🔎 No se encontraron productos con ese nombre.")

    # Muestra todos los productos del inventario.
    def mostrar_todos(self):
        if not self.productos:
            print(" Inventario vacío.")
        else:
            print("\n Lista de productos:")
            self.mostrar_tabla(self.productos)

    # Muestra una lista de productos en formato tabular.
    def mostrar_tabla(self, lista):
        print("-" * 60)
        print(f"{'ID':<10} {'Nombre':<20} {'Cantidad':<10} {'Precio ($)':<10}")
        print("-" * 60)
        for p in lista:
            print(f"{p.id:<10} {p.nombre:<20} {p.cantidad:<10} {p.precio:<10.2f}")
        print("-" * 60)


# Función principal que ejecuta el menú interactivo.
def ejecutar_menu():
    inventario = Inventario()  # Creamos una instancia del inventario.

    while True:  # Bucle infinito hasta que el usuario decida salir.
        print("\n  MENÚ DE INVENTARIO")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")  # Pedimos al usuario que elija una opción.

        if opcion == "1":
            try:
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError as e:
                print(f"❗ Entrada inválida: {e}")

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            try:
                nueva_cantidad = int(cantidad) if cantidad else None
                nuevo_precio = float(precio) if precio else None
                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)
            except ValueError as e:
                print(f" Entrada inválida: {e}")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print(" ¡Hasta luego!")
            break

        else:
            print("⚠ Opción inválida.")

        # Punto de entrada del programa
if __name__ == "__main__":
        ejecutar_menu()