class Proveedores:
    def __init__(self, nombreProveedor, telefonoProveedor, emailProveedor):
        self.nombreProveedor = nombreProveedor
        self.telefonoProveedor = telefonoProveedor
        self.emailProveedor = emailProveedor
        
    def getNombreProveedor(self):
        return self.nombreProveedor
    
    def getTelefonoProveedor(self):
        return self.telefonoProveedor
    
    def getEmailProveedor(self):
        return self.emailProveedor
    
    def setNombreProveedor(self, nombreProveedor):
        self.nombreProveedor = nombreProveedor
        
    def setTelefonoProveedor(self, telefono):
        self.telefonoProveedor = telefono
        
    def setEmailProveedor(self, email):
        self.emailProveedor = email