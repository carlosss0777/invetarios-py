class Productos:
    def __init__(self, nombreProducto, stockProducto, proveedorProducto, precioProducto, descripcionProducto):
        self._nombreProducto = nombreProducto
        self._stockProducto = stockProducto
        self._proveedorProducto = proveedorProducto
        self._precioProducto = precioProducto
        self._descripcionProducto = descripcionProducto
        
    @property
    def nombreProducto(self):
        return self._nombreProducto
    
    @property
    def stockProducto(self):
        return self._stockProducto
    
    @property
    def proveedorProducto(self):
        return self._proveedorProducto
    
    @property
    def precioProducto(self):
        return self._precioProducto
    
    @property
    def descripcion(self):
        return self._descripcionProducto
    
    @nombreProducto.setter
    def nombreProducto(self, nombre):
        self._nombreProducto = nombre

    @stockProducto.setter
    def stockProducto(self, stock):
        self._stockProducto = stock
        
    @proveedorProducto.setter
    def proveedorProducto(self, proveedor):
        self._proveedorProducto = proveedor
        
    @precioProducto.setter
    def precioProducto(self, precio):
        self._precioProducto = precio

    @descripcion.setter  
    def descripcion(self, descripcion):
        self._descripcionProducto = descripcion