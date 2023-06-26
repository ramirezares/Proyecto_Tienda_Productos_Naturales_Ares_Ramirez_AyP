import requests
from Functions import *
from Functions import product_management_module
from Functions import customer_management_module


from Product import Product

#TODO: Hacer modulo Stat "from Stat import Stat"


class NaturalProductsOnlineShop:
    """_summary_
    Clase "Tienda": NaturalProductsOnlineShop.
    
    Args: 
    Products=[]
    Costumers=[]
    Sales=[]
    Bills=[]
    Payments=[]
    Shipped=[]
    Stats=[]
    
    Metodos: 
    Ver en el diagrama       #export_atr? Preguntar si lo elimino(show_atr) #TODO: Copiar los metodos
    """
    
    def __init__(self):
        """_Crea una instancia de la clase NaturalProductsOnlineShop_
        """
        self.Products= []
        self.Customers= []
        self.Sales= []
        self.payments=[]
        self.Shipped= []
        self.Stats= []
        self.date=None

    def upload_data(self):
        """_summary_
        """

        if len(self.Products)>0:
            self.Products.clear()
        
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json"
        response = requests.get(url)
        data=response.json()
    
        for dicc in data:
            name=dicc["name"]
            description=dicc["description"]
            price=dicc["price"]
            category=dicc["category"]
            new_product=Product(name,description,price,category)
            self.Products.append(new_product)

        print('''
        Precargado de datos completado.
        ''')

        # Poner opcion de cargar los cambios que se habian realizado
    
    def set_date(self):
        set_date()
        
        #self.date

    def product_management(self):   #Gestion de productos # TODO: Hacer docstring
        product_management_module(self)

    def sales_management(self):      #Gestion de ventas Registrar venta. Generar Factura Buscar venta (filtros) 
        # TODO: Hacer docstring
        while True:
            print('''\n -----Bienvenido al modulo de Gestion de Ventas----- \n''')
            options=['Registrar venta.','Generar Factura','Buscar Venta.','Salir.']
            print_options(options)
            chose=input('''\n Ingrese la opcion deseada:''')
            while not chose.isnumeric() or int(chose) not in range(1,len(options)+1):
                chose=input('''\n Opcion invalida. Ingrese la opcion deseada:\n Ingrese 0 Para salir \n''')
                if chose=='0':
                    break
            
            if chose=='1': #Registrar Venta
                print(f'Hola {1}')
            
            if chose=='2': #Generar Factura
                print(f'Hola {2}')
            
            if chose=='3': #Buscar venta 
                print(f'Hola {3}')

            if chose=='4': #Salir 
                break

    def customer_management(self):      #Gestion de clientes Mismo que productos
        # TODO: Hacer docstring
        customer_management_module(self)

    def payment_management(self):      #Gestion de pagos
        # TODO: Hacer docstring
        pass

    def shipping_management(self):      #Gestion de envios
        # TODO: Hacer docstring
        pass

    def stats_management(self):      #Estadisticas
        # TODO: Hacer docstring
        pass

    #necesito un registro? Para el modulo estadisticas?

    def menu(self):     #Menu
        # TODO: Hacer docstring
        while True:
            print('''
----------Bienvenido a la Tienda Online de Productos Naturales: Natural Shop----------
¿Que desea hacer?
''')
            options=['Restablecer','Gestion de productos','Gestion de ventas','Gestion de clientes','Gestion de pagos','Gestion de envios','Estadisticas','Salir',]
            print_options(options)
            chose=input(f'''\n Ingrese el numero de la opcion deseada:''')
            while not chose.isnumeric() or int(chose) not in range(1,len(options)+1):
                chose=input(f'''\n Opcion invalida. Ingrese el numero de la opcion deseada:''')
            if chose=='1': # Cargar con API metodo upload_data
                self.upload_data()
            if chose=='2': # Gestion de productos
                self.product_management()
            if chose=='3': # Gestion de ventas
                self.sales_management()

            if chose=='4': # Gestion de clientes
                self.customer_management()
            
            if chose=='5': # Gestion de pagos 
                pass
            
            if chose=='6': # Gestion de envios
                pass
            
            if chose=='7': # Estadisticas
                pass
            
            if chose=='8': # Salir
                break

