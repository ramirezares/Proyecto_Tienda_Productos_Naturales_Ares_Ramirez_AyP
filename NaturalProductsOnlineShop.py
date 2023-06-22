import requests
from Functions import print_options
from Functions import is_int
from Functions import is_float

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
        


    def product_management(self):   #Gestion de productos
        # TODO: Hacer docstring
        while True:
            print('''
-----Bienvenido al modulo de Gestion de Productos-----
''')
            options=['Agregar producto.','Buscar producto.','Modificar informacion de un producto.','Eliminar producto.','Salir.']
            print_options(options)
            chose=input('''

Ingrese la opcion deseada:''')
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
                while True:
                    print('''-----Modificacion de atributos-----
                    Seleccione el producto a modificar:
                    ''')
                    for idx in range(len(self.Products)):
                        print(f'{idx+1} {self.Products[idx].show_atr()}')
                    chose=input('Introduzca el numero del producto a modificar')
                    #validar int and in range
                    idx_product_to_modify=int(chose)-1
                    product_to_modify=self.Products[idx_product_to_modify]
                    print('''
                    Seleccione el atributo a modificar:
                    ''')
                    options=['Nombre.','Descripcion','Precio','Categoria','Disponibilidad','Salir']
                    #validar int and in range
                    print_options(options)
                    chose=input('Introduzca el numero del atributo que desea a modificar')
                    product_to_modify.modify_atr(chose)

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
            print('''
----------Bienvenido a la Tienda Online de Productos Naturales: Natural Shop----------
¿Que desea hacer?
''')
            options=['Restablecer','Gestion de productos','Gestion de ventas','Gestion de clientes','Gestion de pagos','Gestion de envios','Estadisticas','Salir',]
            for i in range(len(options)):
                print(f'    {i+1}. {options[i]}')
            chose=input('''
Ingrese el numero de la opcion deseada:''')
            while not chose.isnumeric() and int(chose)+1 not in range(1,len(options)):
                chose=input('''
                Opcion invalida. Ingrese el numero de la opcion deseada:''')
            if chose=='1': # Cargar con API metodo upload_data
                self.upload_data()
            if chose=='2': # Gestion de productos
                self.product_management()
            if chose=='3': # Gestion de ventas
                pass
            if chose=='4': # Gestion de clientes
                self.customer_management()
            
            if chose=='5': # Gestion de pagos 
                pass
            
            if chose=='6': # Gestion de envios
                pass
            
            if chose=='7': # Estadisticas
                pass
            
            if chose=='8': # Salir
                pass

