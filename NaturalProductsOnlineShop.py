import requests
from Functions import *

from Product import Product
from Sale import Sale
from LegalSale import LegalSale

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
    
    Metodos: 
    Ver en el diagrama       #export_atr? Preguntar si lo elimino(show_atr) #TODO: Copiar los metodos
    """
    
    def __init__(self):
        """_Crea una instancia de la clase NaturalProductsOnlineShop_
        """
        self.Products= []
        self.Customers= []
        self.Sales= []
        self.Payments=[]
        self.Shipped= []
        self.Stats= []
        self.date=set_date()

    def upload_data(self):
        
        if len(self.Products)>0:
            self.Products.clear()
        print(f'\n -----Precargado de datos-----')
        print(f'\n Cargando. \n')
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json"
        response = requests.get(url)
        data=response.json()
        for dicc in data:
            name=dicc["name"]
            description=dicc["description"]
            price=dicc["price"]
            category=dicc["category"]
            availability=dicc["quantity"]
            new_product=Product(name,description,price,category,availability)
            self.Products.append(new_product)
        print('''Precargado de datos completado.''')
        # Poner opcion de cargar los cambios que se habian realizado con el txt

    def start(self):
        self.upload_data()
        self.menu()

    def product_management(self):   #Gestion de productos # TODO: Hacer docstring
        while True:
            print(f'''\n-----Bienvenido al modulo de Gestion de Productos-----\n''')
            options=['Agregar producto.','Buscar producto.','Modificar informacion de un producto.','Eliminar producto.','Salir.']
            print_options(options)
            chose=input('''\nIngrese la opcion deseada:''')
            while not chose.isnumeric() or int(chose) not in range(1,len(options)+1):
                chose=input('''\nOpcion invalida. Ingrese la opcion deseada:\nIngrese 0 Para salir
                    ''')
                if chose=='0':
                    break
            if chose=='1': # Agregar producto
                   new_product=add_product()
                   self.Products.append(new_product)
                   
            if chose=='2': # Buscar Producto
                   search_product(self)
    
            if chose=='3': # Modificar inf producto
                  modify_product(self)
                  
            if chose=='4': # Eliminar producto
                  del_product(self)
                  print(f'\nEliminado')
    
            if chose=='5': # Salir
                  break

    def sales_management(self):      #Gestion de ventas # TODO: Hacer docstring
        while True:
            print('''\n -----Bienvenido al modulo de Gestion de Ventas----- \n''')
            options=['Registrar venta.','Generar Factura','Buscar Venta.','Salir.']
            print_options(options)
            chose=input('''\n Ingrese la opcion deseada:''')
            while not chose.isnumeric() or int(chose) not in range(1,len(options)+1):
                chose=input(f'\n Opcion invalida. Ingrese la opcion deseada:')
                    
            if chose=='1': #Registrar Venta
                if len(self.Customers)>0:
                    print(f'\n -----Seleccion del tipo de venta-----\n')
                    options=['Venta Natural','Venta Juridica','Salir']
                    print_options(options)
                    chose=input(f'\n Ingrese el numero de la opcion deseada:')
                    while not is_int(chose) or int(chose) not in range(1,len(options)+1):
                        chose=input(f'\n Invalido. Ingrese el numero de la opcion deseada:')
                    if chose=='1': #Natural sale date,saleNumber,customer(Natural),products(lista),paymentMethod,shippingMethod
                        date=self.date
                        saleNumber=calculate_saleNumber(self)
                        customer=select_naturalCustomer(self)
                        products=select_products(self)
                        paymentMethod=select_paymentMethod()
                        shippingMethod=select_shippingMethod()
                        new_sale=Sale(date,saleNumber,customer,products,paymentMethod,shippingMethod)
                        self.Sales.append(new_sale)
                        print(f'\n-Venta Registrada-\n')
                        generate_bill(self,sale=new_sale,val=True)
                    if chose=='2': #Legal date,saleNumber,customer,products,paymentMethod,shippingMethod,amount_of_days
                        date=self.date
                        saleNumber=calculate_saleNumber(self)
                        customer=select_legalCustomer(self)
                        products=select_products(self)
                        paymentMethod=select_paymentMethod()
                        shippingMethod=select_shippingMethod()
                        print(f'\n   -Pago de contado-   \n')
                        amount_of_daysOptions=[15,30]
                        print_options(amount_of_daysOptions)
                        amount_of_days=input(f'\nIngrese el numero de dias para pago de contado:')
                        while not is_int(amount_of_days) or int(amount_of_days) not in amount_of_daysOptions:
                            amount_of_days=input('Invalido. Ingrese una de las dos opciones (15 o 30 dias):')
                        new_sale=LegalSale(date,saleNumber,customer,products,paymentMethod,shippingMethod,int(amount_of_days))
                        self.Sales.append(new_sale)
                        print(f'\n-Venta Registrada-\n')
                        generate_bill(self,new_sale,True)
                    if chose=='3':
                         break
                else:
                      print(f'\n No hay clientes registrados. Por favor registre un cliente antes de registrar una venta.')
                      new_customer=add_customer(self)
                      self.Customers.append(new_customer)
                      print(f'\n Registrado. \n')
            if chose=='2': #Generar Factura
                 sale=None               
                 generate_bill(self,sale,False) #sale y val son variables creadas para dirigir el codigo. Ver la funcion en Functions 

            if chose=='3': #Buscar venta 
                search_sale(self)

            if chose=='4': #Salir 
                break

    def customer_management(self):      #Gestion de clientes # TODO: Hacer docstring
        while True:
            print(f'''\n-----Bienvenido al modulo de Gestion de Clientes-----\n''')
            options=['Agregar cliente.','Buscar cliente.','Modificar informacion de un cliente.','Eliminar cliente.','Salir.']
            print_options(options)
            chose=input('''\nIngrese la opcion deseada:''')
            while not chose.isnumeric() or int(chose) not in range(1,len(options)+1):
                chose=input(f'\nOpcion invalida. Ingrese la opcion deseada:')
                if chose=='0':
                    break
            if chose=='1': # Agregar cliente
                   new_customer=add_customer(self)
                   self.Customers.append(new_customer)
                   print(f'\n Registrado. \n')

            if chose=='2': # Buscar cliente
                   search_customer(self)

            if chose=='3': # Modificar inf cliente
                  modify_customer(self)

            if chose=='4': # Eliminar cliente
                  del_customer(self)

            if chose=='5': # Salir
                  break

    def payment_management(self):      #Gestion de pagos
        while True:
            print('''\n -----Bienvenido al modulo de Gestion de Pagos----- \n''')
            options=['Registrar pago.','Buscar pago.','Salir.']
            print_options(options)
            chose=input('''\n Ingrese la opcion deseada:''')
            while not chose.isnumeric() or int(chose) not in range(1,len(options)+1):
                 chose=input(f'\n Opcion invalida. Ingrese la opcion deseada:')
            if chose=='1': # Registrar pago
                if len(self.Sales)>0:
                    print('-Registro de pago-')
                    aux=0
                    for sale in self.Sales:
                        print(f'{aux+1} {sale.saleNumber} {sale.customer} {sale.customer.identifierDocument} {sale.breakdown}')
                        aux+=1
                    chose=input(f'\nIngrese la venta deseada:')
                    while not is_int(chose) or int(chose) not in range(1,len(self.Sales)+1):
                        chose=input(f'\n Invalido. Ingrese el numero la venta deseada:')
                    sale=self.Sales[int(chose)-1]

                    date=self.date
                    payNumber=sale.saleNumber
                    customer=sale.customer
                    paymentType=sale.paymentMethod
                    paymentCurrency=get_paymentCurrency(sale)
                    total=sale.breakdown['Total']
                    if type(sale)==LegalSale:
                        print('-Seleccione el estado del pago-')
                        options=['Pagado','Por pagar']
                        print_options(options)
                        chose=input('Ingrese el numero de la opcion:')
                        while int(chose) not in range(1,len(options)+1):
                             chose=input('Ingrese la opcion:')
                        payStatus=options[int(chose)-1]
                    else:
                        payStatus='Pagado'
                    new_pay=Pay(date,payNumber,customer,paymentType,paymentCurrency,total,payStatus)
                    self.Payments.append(new_pay)
                    print('Registrado.')
                else:
                     print('No hay ventas registradas. Por favor registre una venta antes de un pago.')
            if chose=='2': # Buscar pago
                 if len(self.Shipped)>0:
                      pass
                 else:
                      print('No hay pagos registrados.')
            if chose=='3': # Salir
                 break

    def shipping_management(self):      #Gestion de envios
        while True:
            print('''\n -----Bienvenido al modulo de Gestion de Envios----- \n''')
            options=['Registrar envio.','Buscar envio.','Salir.']
            print_options(options)
            chose=input('''\n Ingrese la opcion deseada:''')
            while not chose.isnumeric() or int(chose) not in range(1,len(options)+1):
                 chose=input(f'\n Opcion invalida. Ingrese la opcion deseada:')
            if chose=='1':
                 if len(self.Sales)>0:
                    print('-Registro de envio-')
                    aux=0
                    for sale in self.Sales:
                        print(f'{aux+1} {sale.saleNumber} {sale.customer} {sale.customer.identifierDocument} {sale.breakdown}')
                        aux+=1
                    chose=input(f'\nIngrese la venta deseada:')
                    while not is_int(chose) or int(chose) not in range(1,len(self.Sales)+1):
                         chose=input(f'\n Invalido. Ingrese el numero la venta deseada:')
                    sale=self.Sales[int(chose)-1]

                    date=self.date
                    shippingNumber=sale.saleNumber
                    shippingService=sale.shippingMethod
                    shippingCost=calculate_shippingCost(sale)

                    
                 else:
                      print('No hay ventas registradas. Por favor registre una venta antes de un envio.')
            if chose=='2': # Buscar envio  segun: cliente, fecha
                 if len(self.Shipped)>0:
                      pass
                 else:
                      print('No hay envios registrados.')
            
            if chose=='3': #Salir
                break


    def stats_management(self):      #Estadisticas
        # TODO: Hacer docstring
        pass

    def menu(self):     #Menu   # TODO: Hacer docstring
        while True:
            print(f'\n----------Bienvenido a la Tienda Online de Productos Naturales: Natural Shop----------\n¿Que desea hacer?')
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
                self.payment_management()
            
            if chose=='6': # Gestion de envios
                self.shipping_management()
            
            if chose=='7': # Estadisticas
                pass
            
            if chose=='8': # Salir
                break

