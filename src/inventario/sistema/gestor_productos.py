from inventario.modelos.productos import Productos

class gestor_productos:
    def __init__(self):
        self.lista_productos = []

    def validarNombreProducto(self, nombre):
        if not nombre:
            raise ValueError("Error: el nombre no puede estar vacio")
        
        if not nombre.isApha():
            raise ValueError("Error: el nombre debe contener unicamente letras")
        
    def validarStock(self, stock):
        if not stock:
            raise ValueError("Error: el stock no puede estar vacio")
        
        if not stock.is_integer():
            raise ValueError("Error: el stock deben ser numeros ")
