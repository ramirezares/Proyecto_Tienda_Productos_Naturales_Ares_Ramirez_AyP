import requests
import pickle
from Functions import *

from Product import Product
from Sale import Sale
from LegalSale import LegalSale
from Pay import Pay
from Shipping import Shipping


class NaturalProductsOnlineShop:
    """Clase "Tienda": NaturalProductsOnlineShop.
    
    Args: 
    Products=[]
    Costumers=[]
    Sales=[]
    Bills=[]
    Payments=[]
    Shipped=[]
    
    Metodos: 
    print_options(options:list): 
    calculate_deadline(saleTime,today:Date,amount_of_days:int)
    set_date()
    add_product()
    search_product_with_filter(self,filter:str)
    search_product(self)
    modify_product(self)
    del_product(self)
    add_customer(self)
    search_customer(self)
    chosing_atr(options:list,)
    modify_customer(self): 
    del_customer(self)
    generate_bill(self)
    generate_final_bill(sale)
    calculate_saleNumber(self)
    define_selected_customer(self,id)
    select_naturalCustomer(self)
    select_legalCustomer(self)
    select_products(self)
    select_paymentMethod()
    select_shippingMethod()
    build_Products_breakdown(products:list)
    calculate_subtotal(products)
    calculate_SaletotalAmount(subtotal,IVA,IGFT)
    calculate_LegalSaletotalAmount(subtotal,discount,IVA,IGFT,val)
    build_SaletotalAmount_breakdown(paymentMethod,products)
    calculate_discount(saleTime)
    build_LegalSaletotalAmount_breakdown(paymentMethod,discount,products)
    search_sale(self)
    get_paymentCurrency(sale)
    calculate_payNumber(self)
    search_pay(self)
    search_and_verf_pay(self,sale)
    calculate_shippingCost(sale)
    register_delivery()
    search_shipping(self)
    selection_period_to_search_and_generate_inf(self):
    report_sales_number_in_year(self,years_to_print,months_to_print,date_init:Date,date_final:Date):
    report_sales_number_in_month(self,yearNumber,monthNumber,date_init:Date,date_final:Date):
    report_pay_number_in_year(self,years_to_print,months_to_print,date_init:Date,date_final:Date):
    report_pay_number_in_month(self,yearNumber,monthNumber,date_init:Date,date_final:Date):
    report_shipping_number_in_year(self,years_to_print,months_to_print,date_init:Date,date_final:Date):
    report_shipping_number_in_month(self,yearNumber,monthNumber,date_init:Date,date_final:Date):
    """
    
    def __init__(self):
        """_Crea una instancia de la clase NaturalProductsOnlineShop_
        """
        self.Products= []
        self.Customers= []
        self.Sales= []
        self.Payments=[]
        self.Shipped= []
        self.date=set_date()

    def start(self):
        self.get_data_of_txt()
        self.menu()

    def upload_data_with_API(self):
        
        if len(self.Products)>0:
            self.Products.clear()
        print(f'\n -----Precargado de datos de inicializacion-----')
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
        print(f'\nPrecargado de datos completado.\n')
        while True:
             decition=input(f'\nDesea cargar los datos de la tienda guardados localmente(y/n):')
             if decition=='y':
                  self.get_data_of_txt()
                  break
             elif decition=='n':
                  break
             else:
                  continue

    def save_data_in_txt(self):
         dates_of_program_to_save=[self.Products,self.Customers,self.Sales,self.Payments,self.Shipped]

         file_name='/home/ramirezares/Proyecto_Tienda_Productos_Naturales_Ares_Ramirez_AyP/dates_of_program.pickle'

         with open(file_name,'wb') as g:
              pickle.dump(dates_of_program_to_save,g)
         print(f'\n-Guardado finalizado-')

    def get_data_of_txt(self):
        print('\n Cargando...')

        file_name='/home/ramirezares/Proyecto_Tienda_Productos_Naturales_Ares_Ramirez_AyP/dates_of_program.pickle'

        with open(file_name,'rb') as g:
            dates_of_program_to_get=pickle.load(g)
            self.Products=dates_of_program_to_get[0]
            self.Customers=dates_of_program_to_get[1]
            self.Sales=dates_of_program_to_get[2]
            self.Payments=dates_of_program_to_get[3]
            self.Shipped=dates_of_program_to_get[4]
        print(f'\n Lectura finaliza.')
         
         
    def product_management(self):   #Gestion de productos
        while True:
            print(f'''\n-----Bienvenido al modulo de Gestion de Productos-----\n''')
            options=['Agregar producto.','Buscar producto.','Modificar informacion de un producto.','Eliminar producto.','Salir.']
            print_options(options)
            chose=input('''\nIngrese la opcion deseada:''')
            while not chose.isnumeric() or int(chose) not in range(1,len(options)+1):
                chose=input(f'\nOpcion invalida. Ingrese la opcion deseada:\nIngrese 0 Para salir:')
                if chose=='0':
                    break
            if chose=='1': # Agregar producto
                   new_product=add_product()
                   self.Products.append(new_product)
                   print(f'\n Producto registrado. \n')
                   
            if chose=='2': # Buscar Producto
                   search_product(self)
    
            if chose=='3': # Modificar inf producto
                  modify_product(self)
                  
            if chose=='4': # Eliminar producto
                  del_product(self)
                  print(f'\nEliminado')
    
            if chose=='5': # Salir
                  break

    def sales_management(self):      #Gestion de ventas
        while True:
            print(f'\n -----Bienvenido al modulo de Gestion de Ventas----- \n')
            options=['Registrar venta.','Generar Factura','Buscar Venta.','Salir.']
            print_options(options)
            chose=input('''\n Ingrese la opcion deseada:''')
            while not chose.isnumeric() or int(chose) not in range(1,len(options)+1):
                chose=input(f'\n Opcion invalida. Ingrese la opcion deseada:')
                    
            if chose=='1': #Registrar Venta
                    print(f'\n -----Seleccion del tipo de venta-----\n')
                    options=['Venta a cliente natural','Venta a cliente juridico','Salir']
                    print_options(options)
                    chose_clas=input(f'\n Ingrese el numero de la opcion deseada:')
                    while not is_int(chose_clas) or int(chose_clas) not in range(1,len(options)+1):
                        chose_clas=input(f'\n Invalido. Ingrese el numero de la opcion deseada:')
                    if chose_clas=='1': #Natural sale date,saleNumber,customer(Natural),products(lista),paymentMethod,shippingMethod
                        date=self.date
                        saleNumber=calculate_saleNumber(self)
                        saleStatus='Pagado'
                        customer=select_naturalCustomer(self)
                        products=select_products(self)
                        paymentMethod=select_paymentMethod()
                        shippingMethod=select_shippingMethod()
                        new_sale=Sale(date,saleNumber,saleStatus,customer,products,paymentMethod,shippingMethod)
                        self.Sales.append(new_sale)
                        print(f'\n Venta registrada. \n')
                        generate_final_bill(new_sale) 
                    if chose_clas=='2': #Legal 
                        date=self.date
                        saleNumber=calculate_saleNumber(self)
                        customer=select_legalCustomer(self)
                        print('') 
                        options=['Pago de contado','Pago a credito'] #Para determinar saleTime y saleStatus
                        print_options(options)
                        chose_kind=input(f'\nSeleccione la opcion deseada:')
                        while not is_int(chose_kind) or int(chose_kind) not in range(1,len(options)+1):
                             chose_kind=input(f'\nInvalido. Seleccione la opcion deseada:')
                        if chose_kind=='1':
                             saleTime=options[int(chose_kind)-1]
                             saleStatus='Pagado'
                             amount_of_days=0
                        else:
                            saleTime=options[int(chose_kind)-1]
                            saleStatus='Pendiente'
                            print(f'\n   -Pago a credito-   \n Plazos (en dias):')
                            amount_of_daysOptions=[15,30]
                            print_options(amount_of_daysOptions)
                            amount_of_days=input(f'\nIngrese el numero de la opcion deseada:')
                            while not is_int(amount_of_days) or int(amount_of_days) not in amount_of_daysOptions:
                                 amount_of_days=input('Invalido. Ingrese una de las dos opciones (15 o 30 dias):')                                          
                                                
                        products=select_products(self)
                        paymentMethod=select_paymentMethod()
                        shippingMethod=select_shippingMethod()
                        
                        new_sale=LegalSale(date,saleNumber,saleTime,saleStatus,customer,products,paymentMethod,shippingMethod,int(amount_of_days))
                        self.Sales.append(new_sale)
                        print(f'\n Venta registrada. \n')
                        generate_final_bill(new_sale)         
                    
                    if chose_clas=='3':
                         break
                    
            if chose=='2': #Generar Factura     
                generate_bill(self) #sale y val son variables creadas para dirigir el codigo. Ver la funcion en Functions 

            if chose=='3': #Buscar venta 
                search_sale(self)

            if chose=='4': #Salir 
                break

    def customer_management(self):      #Gestion de clientes
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
                   if type(new_customer)==Natural:
                        self.Customers.append(new_customer)
                        print(f'\n Cliente registrado. \n')
                   elif type(new_customer)==Legal:
                        self.Customers.append(new_customer)
                        print(f'\n Cliente registrado. \n')
                   else:
                        print(f'\n No se pudo registrar el cliente. \n')                        

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
            print(f'\n -----Bienvenido al modulo de Gestion de Pagos----- \n')
            options=['Registrar pago.','Buscar pago.','Salir.']
            print_options(options)
            chose=input(f'\n Ingrese la opcion deseada:')
            while not chose.isnumeric() or int(chose) not in range(1,len(options)+1):
                 chose=input(f'\n Opcion invalida. Ingrese la opcion deseada:')
            if chose=='1': # Registrar pago
                if len(self.Sales)>0:
                    print(f'\n-Registro de pago-\n')
                    for sale in self.Sales:
                        print(f'{sale.saleNumber} {sale.customer.name} {sale.customer.identifierDocument} {sale.breakdown}')
                    chosed=input(f'\nIngrese la venta:')
                    while not is_int(chosed) or int(chosed) not in range(1,len(self.Sales)+1):
                         chosed=input(f'\n Invalido. Ingrese el numero la venta deseada:')
                    sale=self.Sales[int(chosed)-1]
                    self.Sales[int(chosed)-1].saleStatus='Pagado'
                    
                    date=self.date
                    payNumber=sale.saleNumber  #Asumiendo que en el pago a credito solo se puede pagar en una cuota que la paga el cliente en el momento del registro del pago
                    customer=sale.customer
                    paymentType=sale.paymentMethod
                    paymentCurrency=get_paymentCurrency(sale)
                    total=sale.breakdown['Total']
                    new_pay=Pay(date,payNumber,customer,paymentType,paymentCurrency,total)
                    not_is_in_payments=True
                    for pay in self.Payments:
                         if pay.payNumber==new_pay.payNumber:
                              print(f'\nLa venta ya tiene un pago registrado:')
                              not_is_in_payments=False
                              break
                         else:
                              not_is_in_payments=True
                    if not_is_in_payments:
                         print(new_pay.show_atr())
                         self.Payments.append(new_pay)
                         print(f'\n Pago registrado. \n')
                else:
                     print(f'\nNo hay ventas registradas. Por favor registre una venta antes de un pago.')
            
            if chose=='2': # Buscar pago
                 search_pay(self)

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
                    print(f'\n-Registro de envio-\n')
                    for sale in self.Sales:
                        print(f'{sale.saleNumber} {sale.customer.name} {sale.customer.identifierDocument} {sale.breakdown}')
                    chosed=input(f'\nIngrese la venta deseada:')
                    while not is_int(chosed) or int(chosed) not in range(1,len(self.Sales)+1):
                         chosed=input(f'\n Invalido. Ingrese el numero la venta deseada:')
                    sale=self.Sales[int(chosed)-1]
                    
                    pay_in_payments=search_and_verf_pay(self,sale)

                    if pay_in_payments:
                         sale.saleStatus='Enviado'
                         date=self.date
                         customer=sale.customer
                         order=sale
                         shippingNumber=sale.saleNumber
                         shippingService=sale.shippingMethod
                         shippingCost=calculate_shippingCost(sale)
                         new_shipping=Shipping(date,customer,shippingNumber,order,shippingService,shippingCost)
                         not_is_in_shipping=True
                         for shipping in self.Shipped:
                              if shipping.shippingNumber==new_shipping.shippingNumber:
                                   print('La venta ya tiene un envio registrado:')
                                   not_is_in_shipping=False
                                   break
                              else:
                                   not_is_in_shipping=True
                         if not_is_in_shipping:
                              print(new_shipping.show_atr())
                              self.Shipped.append(new_shipping)
                              print(f'\n Envio registrado. \n')
                    else:
                         print(f'\nNo hay pago registrado para esta venta. Registre el pago antes de enviar.')
                    
                 else:
                      print('No hay ventas registradas. Por favor registre una venta antes de un envio.')
            if chose=='2': # Buscar envio  
                 search_shipping(self)
                      
            if chose=='3': #Salir
                break


    def stats_management(self):      #Estadisticas 
         while True:
            print('''\n -----Bienvenido al modulo de Estadisticas----- \n''')
            options=['Generar informe de ventas.','Generar informe de pagos.','Generar informe de envios','Salir.']
            print_options(options)
            chose=input('''\n Ingrese la opcion deseada:''')
            while not chose.isnumeric() or int(chose) not in range(1,len(options)+1):
                chose=input(f'\n Opcion invalida. Ingrese la opcion deseada:')
    
            if chose=='1':  #   INFORME DE VENTAS

                years_to_print,months_to_print,date_init,date_final=selection_period_to_search_and_generate_inf(self)
                
                print(f'\n ------------------------------------------------------------Informe de Ventas------------------------------------------------------------ \n')
                
                report_sales_number_in_year(self,years_to_print,months_to_print,date_init,date_final)
                
                print(f'\n---------------Productos mas vendidos (Producto:Cantidad vendida)--------------- \n')
                most_saled_productsAmount={}
                for sale in self.Sales:
                    for product in sale.products:
                         nameProduct=product['name']
                         amountProduct=product['amount']
                         if nameProduct not in most_saled_productsAmount:
                              most_saled_productsAmount[f'{nameProduct}']=amountProduct
                         else:
                              most_saled_productsAmount[f'{nameProduct}']+=amountProduct
                print(most_saled_productsAmount)

                print(f'\n---------------Clientes mas frecuentes (Documento de identificacion del cliente:Cantidad de compras)---------------\n')
            
                customers_most_frecuent={}
                for sale in self.Sales:
                     customerID=sale.customer.identifierDocument
                     if customerID not in customers_most_frecuent:
                          customers_most_frecuent[f'{customerID}']=1
                     else: 
                          customers_most_frecuent[f'{customerID}']+=1
                print(customers_most_frecuent)

            if chose=='2': #    INFORME DE PAGOS 

                years_to_print,months_to_print,date_init,date_final=selection_period_to_search_and_generate_inf(self)

                print(f'\n ------------------------------------------------------------Informe de Pagos------------------------------------------------------------ \n')
  
                report_pay_number_in_year(self,years_to_print,months_to_print,date_init,date_final)

                print(f'\n---------------Clientes con pagos pendientes---------------\n')
                customers_with_pending_pay=[]
                for sale in self.Sales:
                    salePending=sale
                    customers_with_pending_pay.append(salePending)
                if len(self.Payments)>0:
                     for salePending in customers_with_pending_pay:
                          for pay in self.Payments:
                               if salePending.saleNumber in pay.payNumber:
                                    i=customers_with_pending_pay.index(salePending)
                                    customers_with_pending_pay.pop(i)
                if len(customers_with_pending_pay)>0:
                     for salePending in customers_with_pending_pay:
                          print(f'{salePending.customer.name} {salePending.customer.identifierDocument}. Fecha de la venta: {salePending.date.show_date()}')
                else: 
                     print('No hay clientes con pagos pendientes')

            if chose=='3': #    INFORME DE ENVIOS 
                 
                 years_to_print,months_to_print,date_init,date_final=selection_period_to_search_and_generate_inf(self)

                 print(f'\n ------------------------------------------------------------Informe de Envios------------------------------------------------------------ \n')

                 report_shipping_number_in_year(self,years_to_print,months_to_print,date_init,date_final)

                 print(f'\n---------------Productos mas enviados---------------\n') 
                 
                 products_most_frecuent={}
                 for sale in self.Sales:
                    for dic in sale.products:
                        productName=dic['name']    
                        productAmount=dic['amount']                
                        if productName not in products_most_frecuent:
                             products_most_frecuent[f'{productName}']=productAmount
                        else: 
                             products_most_frecuent[f'{productName}']+=productAmount
                 print(products_most_frecuent)
                
                 print(f'\n---------------Clientes con envios pendientes---------------\n')
                 customers_with_pending_shipping=[]
                 for sale in self.Sales:
                      if sale.saleStatus!="Enviado":
                        salePending_for_shipping=sale
                        if salePending_for_shipping not in customers_with_pending_shipping:
                             customers_with_pending_shipping.append(salePending_for_shipping)
                 for salePending_for_shipping in customers_with_pending_shipping:
                     print(f'{salePending_for_shipping.customer.name} {salePending_for_shipping.customer.identifierDocument}. Fecha: {salePending_for_shipping.date.show_date()}')
            
            if chose=='4': #Salir
                 break
        

    def menu(self):     #Menu  
        while True:
            print(f'\n----------Bienvenido a la Tienda Online de Productos Naturales: Natural Shop----------\n¿Que desea hacer?\n')
            options=['Restablecer estado inicial del almacen','Gestion de productos','Gestion de ventas','Gestion de clientes','Gestion de pagos','Gestion de envios','Indicadores de gestion (Estadisticas)','Salir',]
            print_options(options)
            chose=input(f'''\n Ingrese el numero de la opcion deseada:''')
            while not chose.isnumeric() or int(chose) not in range(1,len(options)+1):
                chose=input(f'''\n Opcion invalida. Ingrese el numero de la opcion deseada:''')
            if chose=='1': # Cargar con API metodo upload_data
                self.upload_data_with_API()
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
                self.stats_management()
            
            if chose=='8': # Salir
                self.save_data_in_txt()
                break
