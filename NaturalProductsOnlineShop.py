import requests
import Functions

from Product import Product
from Legal import Legal
from Natural import Natural
from Sale import Sale
from LegalSale import LegalSale
from Pay import Pay
from Shipping import Shipping
from Pay import Pay
#TODO: Hacer modulo Stat "from Stat import Stat"


class NaturalProductsOnlineShop:                        
    """_summary_
    Clase "Tienda": NaturalProductsOnlineShop.
    
    Atributos: 
    Products[]
    Costumers[]
    Sales[]
    Payments[]
    Shipped[]
    Stats[]
    
    Metodos: 
    Ver en el diagrama       #show_atr? Preguntar si lo elimino

    """
    #TODO: Copiar los metodos

    def __init__(self):
        # TODO: Hacer docstring:
        self.Products= []
        self.Costumers= []
        self.Sales= []
        self.Shipped= []
        self.Stats= []

    def upload_data(self):
        """_summary_
        Implementacion de la API.

        Empleando el request obtenemos el json y luego lo convertimos a un dic.
        """

        # TODO: Hacer docstring:

        url = "https://github.com/Algoritmos-y-Programacion-2223-3/api-proyecto/blob/main/products.json"
        
        response = requests.get(url)
        products=list(response)
        
    def product_management(self):   #Gestion de productos
        # TODO: Hacer docstring
        while True:
            print('''
-----Bienvenido al modulo de Gestion de Productos-----
''')
            options=['Agregar producto.','Buscar producto.','Modificar informacion de un producto.','Eliminar producto.','Salir.']
            
            chose=input('Ingrese la opcion deseada:')
            while not chose.isnumeric() or int(chose) not in range(1,len(options)+1):
                chose=input('''
Opcion invalida. Ingrese la opcion deseada:
Ingrese 0 Para salir
                ''')
                if chose=='0':
                    break
            if chose=='1': # Agregar producto
                print(f'Hola {1}')
            if chose=='2': # Buscar Producto
                print(f'Hola {2}')
            if chose=='3': # Modificar inf producto
                print(f'Hola {3}')
            if chose=='4': # Eliminar producto
                print(f'Hola {4}')
            if chose=='5': # Salir
                break
    
    def customer_management(self):      #Gestion de clientes
        # TODO: Hacer docstring
        pass

    def sales_management(self):      #Gestion de ventas
        # TODO: Hacer docstring
        pass

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
            print('Bienvenido a la Tienda Online de Productos Naturales: Natural Shop')
            options=['Restablecer','Gestion de productos','Gestion de ventas','Gestion de clientes','Gestion de pagos','Gestion de envios','Estadisticas','Salir',]
            for i in range(len(options)):
                print(f'{i+1}. {options[i]}')
            chose=input('Ingrese el numero de la opcion deseada:')
            while not chose.isnumeric() and int(chose)+1 not in range(1,len(options)):
                chose=input('Opcion invalida. Ingrese el numero de la opcion deseada:')
            if chose=='1': # Cargar con API metodo upload_data
                pass

            if chose=='2': # Gestion de productos
                pass
            
            if chose=='3': # Gestion de ventas
                pass
            
            if chose=='4': # Gestion de clientes
                pass
            
            if chose=='5': # Gestion de pagos 
                pass
            
            if chose=='6': # Gestion de envios
                pass
            
            if chose=='7': # Estadisticas
                pass
            
            if chose=='8': # Salir
                pass

