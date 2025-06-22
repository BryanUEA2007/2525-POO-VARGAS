class Producto: #Creamos una clase producto
    def __init__(self, nombre, precio, cantidad):  #Creamos un constructor y colocamos los atributos que necesitaremos
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad


    #Creamos un metodo que nos va mostrar el nombre del producto y el precio
    def mostrar_informacion(self):
        return f"Producto: {self.nombre} - Precio: ${self.precio} - Disponibles: {self.cantidad}"


# Clase para manejar la tienda
class Tienda:
    def __init__(self):
        self.productos = []
        self.caja = 0

    #Hacemos un metodo para agregar el prodcuto
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Se agregó {producto.nombre} al inventario")
    #Creamos un metodo que nos va a mostrar el inventario
    def mostrar_inventario(self):
        print("\n--- Inventario de la Tienda ---")
        for producto in self.productos:   #El bucle for va a recorrer los productos que agregamos
            print(producto.mostrar_informacion())  #Vamos a mostrar los productos que almacenamos

    #Metodo para vender el producto
    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:  #Creamos un for para recorrer los prodcutos
            if producto.nombre == nombre:  #Si el nombre del prodcuto es igual al producto que existe entra al condicional
                if producto.cantidad >= cantidad:
                    producto.cantidad -= cantidad  #Restamos una cantidad del prodcuto que se vendio
                    venta = producto.precio * cantidad
                    self.caja += venta
                    print(f"Venta realizada: {cantidad} {nombre}(s)")
                    print(f"Total: ${venta}")  #Realizamos la venta
                    return
                else:
                    print("No hay suficiente stock")
                    return
        print("Producto no encontrado")


# Ejemplo de uso

    # Crear la tienda
mi_tienda = Tienda()

 # Crear algunos productos
p1 = Producto("Camisa", 25.99, 10)
p2 = Producto("Pantalón", 35.50, 5)

# Agregar productos a la tienda
mi_tienda.agregar_producto(p1)
mi_tienda.agregar_producto(p2)

# Mostrar inventario inicial
mi_tienda.mostrar_inventario()

# Realizar algunas ventas
print("\n--- Realizando Ventas ---")
mi_tienda.vender_producto("Camisa", 2)
mi_tienda.vender_producto("Pantalón", 1)

# Mostrar inventario actualizado
mi_tienda.mostrar_inventario()
print(f"\nDinero en caja: ${mi_tienda.caja}")
