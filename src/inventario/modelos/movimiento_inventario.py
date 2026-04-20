class MovimientoInventario:
    def __init__(self, nombreProducto, tipoMovimiento, cantidad, fecha):
        self.nombreProducto = nombreProducto
        self.tipoMovimiento = tipoMovimiento
        self.cantidad = cantidad
        self.fecha = fecha
        
    def getNombreProducto(self):
        return self.nombreProducto
    
    def getMovimiento(self):
        return self.tipoMovimiento
    
    def getCantidad(self):
        return self.cantidad
    
    def getFecha(self):
        return self.fecha