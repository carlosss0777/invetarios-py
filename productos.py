class Productos:
    def __init__(self, nombreProducto, stockProducto, proveedorProducto, precioProducto, descripcionProducto):
        self.nombreProducto = nombreProducto
        self.stockProducto = stockProducto
        self.proveedorProducto = proveedorProducto
        self.precioProducto = precioProducto
        self.descripcionProducto = descripcionProducto
        
    def getNombre(self):
        return self.nombreProducto
    
    def getStock(self):
        return self.stockProducto
    
    def getProveedor(self):
        return self.proveedorProducto
    
    def getPrecio(self):
        return self.precioProducto
    
    def getDescripcion(self):
        return self.descripcionProducto
    
    def setNombre(self, nombre):
        self.nombreProducto = nombre

    def setStock(self, stock):
        self.stockProducto = stock
        
    def setProveedor(self, proveedor):
        self.proveedorProducto = proveedor
        
    def setPrecioProducto(self, precio):
        self.precioProducto = precio
        
    def setDescripcion(self, descripcion):
        self.descripcionProducto = descripcion