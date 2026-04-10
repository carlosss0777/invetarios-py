from productos import Productos
from proveedores import Proveedores
from movimiento_inventario import MovimientoInventario
from datetime import datetime


class ExceptionsInventary:
    def __init__(self):
        self.listaProductos = []
        self.listProveedores = []
        self.listaMovimientos = []
        self.datosPrueba()

    def datosPrueba(self):
        prov1 = Proveedores("Logitech", "123456789", "ventas@logitech.com")
        prov2 = Proveedores("Razer", "987654321", "soporte@razer.com")
        prov3 = Proveedores("HP", "555123456", "hp@hp.com")

        self.listProveedores.append(prov1)
        self.listProveedores.append(prov2)
        self.listProveedores.append(prov3)

        prod1 = Productos("Mouse Gamer", 50, prov1, 25.99, "Mouse inalámbrico RGB")
        prod2 = Productos("Teclado Mecánico", 30, prov2, 89.99, "Switch verdes, retroiluminado")
        prod3 = Productos("Monitor 24 pulgadas", 15, prov3, 199.99, "Full HD, 75Hz")
        prod4 = Productos("Laptop", 10, prov3, 899.99, "16GB RAM, 512GB SSD")

        self.listaProductos.append(prod1)
        self.listaProductos.append(prod2)
        self.listaProductos.append(prod3)
        self.listaProductos.append(prod4)
        
    def mostrarProveedores(self):
        if not self.listProveedores:
                print("No hay proveedores registrados")
              
        else:
            i = 1
            for proveedor in self.listProveedores:
                print(f"{i}- {proveedor.getNombreProveedor()}")
                i += 1
            
    
    def registrarProducto(self):
        nombreProducto = input("Ingresa el nombre del producto: ")
        
        stockProducto = int(input("Ingresa el stock inicial del producto: "))
        
        self.mostrarProveedores()
        index = int(input("Ingresa el indice del proveedor")) - 1
        proveedor = self.listProveedores[index]

        precio = float(input("Ingresa el precio del producto: "))

        descripcion = input("Ingresa una descripcion del producto: ")

        prod = Productos(nombreProducto, stockProducto, proveedor, precio, descripcion)

        self.listaProductos.append(prod)

    def registrarProveedor(self):
        nombreProveedor = input("Ingresa el nombre del proveedor: ")

        telefono = input("Ingresa el telefono del proveedor: ")

        email = input("Ingresa el email del proveedor: ")

        prov = Proveedores(nombreProveedor, telefono, email)

        self.listProveedores.append(prov)

    def listarProductos(self):
         i = 1

         for producto in self.listaProductos:
              print(f"{i}- {producto.getNombre()}")
              i += 1

    def eliminarProducto(self):
         self.listarProductos()
         index = int(input("Ingresa el indice del producto que quieres eliminar: ")) - 1

         self.listaProductos.pop(index)

    def actualizarPrecio(self):
         self.listarProductos()
         index = int(input("Ingresa el indice del producto: ")) - 1

         nuevo = float(input("Ingresa el nuevo precio del producto: "))

         self.listaProductos[index].setPrecioProducto(nuevo)

    def verStock(self):
         if not self.listaProductos:
              print("No hay stock actualmente")
         else:
              print("--- STOCK ACTUAL ---")
              for producto in self.listaProductos:
                print(f"Nombre del producto: {producto.getNombre()}")
                print(f"Stock actual: {producto.getStock()}")
                print(f"Proveedor del producto: {producto.getProveedor().getNombreProveedor()}")
                print(f"Precio del producto: {producto.getPrecio()}")
                print(f"Descripcion: {producto.getDescripcion()}")
                print("----------------------------------------------------------")
                print("")

    def menuPrincipal(self):
        print("""
            --- SISTEMA DE INVENTARIOS ---
            1- Gestion de productos
            2- Gestion de proveedores
            3- Movimientos de inventario
            0- Salir del sistema
            """)
        
    def menuGestionInventarios(self):
        while True:
            print("""
            -- GESTION DE PRODUCTOS --
            1- Registrar producto
            2- Listar productos
            3- Eliminar producto
            4- Actualizar precio
            5- Ver stock
            0- Volver al menu principal
            """)
        
            opcion = int(input("Elige una opcion: "))

            match opcion:
                case 1:
                    self.registrarProducto()
            
                case 2:
                    self.listarProductos()

                case 3:
                    self.eliminarProducto()

                case 4:
                    self.actualizarPrecio()
            
                case 5:
                    self.verStock()

                case 0:
                    print("")
                    print("---------------------------------")
                    print("Volviendo al menu principal...")
                    print("---------------------------------")
                    break

                case _:
                    print("Error: opcion no valida")

    def menuGestionProveedores(self):
        while True:
            print("""
            -- GESTION DE PROVEEDORES --
            1- Registrar proveedor
            2- Listar proveedores
            3- Eliminar proveedor
            4- Actualizar proveedor
            0- Volver al menu principal
            """)
        
            opcion = int(input("Elige una opcion: "))

            match opcion:
                case 1:
                    self.registrarProveedor()
            
                case 2:
                    pass

                case 3:
                    pass

                case 4:
                    pass

                case 0:
                    print("")
                    print("---------------------------------")
                    print("Volviendo al menu principal...")
                    print("---------------------------------")
                    break

                case _:
                    print("Error: opcion no valida")

    def menuMovimientosInventarios(self):
        while True:
            print("""
            -- GESTION DE PRODUCTOS --
            1- Registrar entrada
            2- Ver historial
            0- Volver al menu principal
            """)
        
            opcion = int(input("Elige una opcion: "))

            match opcion:
                case 1:
                    self.registrarEntradaSalida()
            
                case 2:
                    self.verHistorial()

                case 0:
                    print("")
                    print("---------------------------------")
                    print("Volviendo al menu principal...")
                    print("---------------------------------")
                    break

                case _:
                    print("Error: opcion no valida")

    def run(self):
        while True:
            self.menuPrincipal()
            opcion = int(input("Elige una opcion: "))

            match opcion:
                case 1:
                    self.menuGestionInventarios()

                case 2:
                    self.menuGestionProveedores()

                case 3:
                    self.menuMovimientosInventarios()
        
                case 0:
                    print("Saliendo del sistema...")
                    break

                case _: 
                    print("Error: opcion no valida")

    def registrarEntradaSalida(self):
        print("""-- REGISTRO DE ENTRADAS/SALIDAS --
                    1- Salida
                    2- Entrada
              """)
        opcion = int(input("Ingresa el tipo de registro que deseas hacer: "))

        match opcion:
            case 1:
                self.listarProductos()
                index = int(input("Ingresa el indice del producto: ")) - 1

                tipoMovimiento = "Salida"

                cantidad = int(input("Ingresa la cantidad a restar: "))

                if self.listaProductos[index].getStock() < cantidad:
                    print("Error: no hay suficiente stock")
                    return
                
                newStock = self.listaProductos[index].getStock() - cantidad
                self.listaProductos[index].setStock(newStock)
                fecha = datetime.now()

                nombre = self.listaProductos[index].getNombre()

                mov = MovimientoInventario(nombre, tipoMovimiento, cantidad, fecha)

            case 2:
                self.listarProductos()
                index = int(input("Ingresa el indice del producto: ")) - 1

                tipoMovimiento = "Entrada"

                cantidad = int(input("Ingresa la cantidad a añadir: "))

                newStock = self.listaProductos[index].getStock() + cantidad
                self.listaProductos[index].setStock(newStock)
                fecha = datetime.now()

                nombre = self.listaProductos[index].getNombre()

                mov = MovimientoInventario(nombre, tipoMovimiento, cantidad, fecha)

            case _:
                print("Operacion no valida...")

        self.listaMovimientos.append(mov)

    def verHistorial(self):
        if not self.listaMovimientos:
            print("Aun no se han regitrado movimientos")

        else:
            i = 1
            for mov in self.listaMovimientos:
                fecha = mov.getFecha()
                print("----------------------------------")
                print(f"-- MOVIMIENTO {i} --")
                print(f"Producto: {mov.getNombreProducto()}")
                print(f"Tipo de movimiento: {mov.getMovimiento()}")
                print(f"Cantidad: {mov.getCantidad()}")            
                print(f"Fecha: {fecha.strftime('%Y-%m-%d')}")
                print(f"Hora: {fecha.strftime('%H:%M:%S')}")
                print("----------------------------------")
                i += 1





