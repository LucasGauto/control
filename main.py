#Intento de app de gestion de inventarios xd

#Funcionalidades:
#Registro de productos.
class Producto:
    def __init__(self, nombre, proveedor=None):
        self.nombre=nombre
        self.descripcion=""
        self.precio=None
        self.existencia=None
        self.proveedor = proveedor
    #Metodos magicos
    def __str__(self):
        return str(self.nombre)
    def __eq__(self,other):
        return self.precio == other.precio
    
    #Getters
    def getDescripcion(self):
        return self.descripcion
    def getPrecio(self):
        return {self.precio}
    def getCantidad(self):
        return self.existencia
    def getProveedor(self):
        return self.proveedor
    
    #Setters
    def setDescripcion(self, texto = str):
        self.descripcion = texto
    def setPrecio(self, precio = float):
        self.precio = precio
    def setCantidad(self, cantidad=int):
        if cantidad > 0:
            self.existencia = cantidad
    def setProveedor(self, nombre = str):
        self.proveedor = nombre

class Inventario:
    def __init__(self):
        self.inventario = []

#Registro de proveedores.
#Control de stock.
#Gestion de pedidos.
#Generación de informes.
#Alertas.
#Seguridad.