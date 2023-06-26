from Date import Date
from Product import Product
from Customer import Customer

from Validations import is_productName
from Validations import is_description
from Validations import is_price
from Validations import is_category
from Validations import *

# TODO: Funcion de imprimir menu recibe una lista y un numero

def print_options(options:list):
        """_summary_ # TODO: "Completar"

        Args:
            options (list): _Lista de la cual se desea imprimir las opciones_
        """      
        for i in range(len(options)):
                    print(f'{i+1}. {options[i]}')

def calculate_deadline(today:Date,amount_of_days:int):
        calendary={"1":31,
                   "2":28,
                   "3":31,
                   "4":30,
                   "5":31,
                   "6":30,
                   "7":31,
                   "8":31,
                   "9":30,
                   "10":31,
                   "11":30,
                   "12":31}
        actualDay=today.day
        actualMonth=today.month
        last_pay_day=actualDay+amount_of_days   #Day of deadline
        pay_month=today.month                   #month of deadline
        pay_year=today.year                     #year of deadline
        
        num_of_Day_of_month=calendary[f'{actualMonth}']
        
        if last_pay_day>num_of_Day_of_month:
                last_pay_day-=num_of_Day_of_month
                pay_month+=1
        
        if pay_month>len(calendary):            #Caso en el cual el mes actual es diciembre y el mes de deadline es enero
                 pay_month-=len(calendary)
                 pay_year+=1
        deadline_date=Date(last_pay_day,pay_month,pay_year)
        return deadline_date

def set_date():     #TODO - Elaborar Funcion revisar en Archivo Tienda
      pass

def add_product():
        print('''
-----Agregar producto-----
Ingrese los datos:
''')
        name=input('Ingrese el nombre del producto:')
        while not is_productName(name):
                name=input('Invalido. Ingrese el nombre del producto:')
        description=input('Ingrese la descripcion del producto:')
        while not is_description(description):
                description=input('Invalido. Ingrese la descripcion del producto:')
        price=input('Ingrese el precio del producto:')
        while not is_price(price):
                price=input('Invalido. Ingrese el precio del producto:')
        category=input('Ingrese la categoria del producto:')
        while not is_category(category):
                category=input('Invalido. Ingrese la categoria del producto:')
        new_product=Product(name,description,float(price),category)
        new_product.modify_atr("5")
        return new_product

def search_product_with_filter(self,filter:str):
    if filter=='category':
          matchedAlternatives=[]
          for dic in self.Products:
            if dic.category not in matchedAlternatives:
                  matchedAlternatives.append(dic.category)
          matchedAlternatives.sort()
          print_options(matchedAlternatives)
          chose=input(f'\nSeleccione la opcion deseada:')
          while not chose.isnumeric() or int(chose) not in range(1,len(matchedAlternatives)+1):
              chose=input('''
Opcion invalida. Ingrese la opcion deseada:
                ''')
          categorySelected=matchedAlternatives[int(chose)-1]
          for dic in self.Products:
                 if dic.category==categorySelected:
                       print(dic.show_atr())
    if filter=='price':
          matchedAlternatives=[]
          for dic in self.Products:
            if dic.price not in matchedAlternatives:
                  matchedAlternatives.append(dic.price)
          matchedAlternatives.sort()
          print_options(matchedAlternatives)
          chose=input(f'\nSeleccione la opcion deseada:')
          while not chose.isnumeric() or int(chose) not in range(1,len(matchedAlternatives)+1):
              chose=input('''
Opcion invalida. Ingrese la opcion deseada:
                ''')
          priceSelected=matchedAlternatives[int(chose)-1]
          for dic in self.Products:
                 if dic.price==priceSelected:
                       print(dic.show_atr())
    if filter=='availability':
          matchedAlternatives=[]
          for dic in self.Products:
            if dic.availability not in matchedAlternatives:
                  matchedAlternatives.append(dic.availability)
          matchedAlternatives.sort()
          print_options(matchedAlternatives)
          chose=input(f'\nSeleccione la opcion deseada:')
          while not chose.isnumeric() or int(chose) not in range(1,len(matchedAlternatives)+1):
              chose=input('''
Opcion invalida. Ingrese la opcion deseada:
                ''')
          availabilitySelected=matchedAlternatives[int(chose)-1]
          for dic in self.Products:
                 if dic.availability==availabilitySelected:
                       print(dic.show_atr())
          
def search_product(self):
        while True:
               print(f'''\n -----Buscar producto----- \n''')
               options=['Categoria','Precio','Nombre','Disponibilidad','Salir']
               print_options(options)
               filterMethod=input(f'\n Ingrese la opcion deseada:')
               while not filterMethod.isnumeric() or int(filterMethod) not in range(1,len(options)+1):
                   filterMethod=input('Invalido. Ingrese el numero de la opcion deseada:')
               if filterMethod=='1':      # Filter is category
                     filter='category'
                     search_product_with_filter(self,filter)

               if filterMethod=='2':      # Filter is price
                     filter='price'
                     search_product_with_filter(self,filter)

               if filterMethod=='3':      # Filter is Name
                      name=input('Introduzca el nombre a buscar:')
                      while not is_productName(name):
                             name=input('Invalido. Introduzca el nombre a buscar:')    
                      sum=0
                      for dic in self.Products:
                             if name in dic.name:
                                    sum+=1
                                    print(dic.show_atr())
                      if sum==0:
                             print(f'\n No hay productos con dicho nombre.')

               if filterMethod=='4':      # Filter is availavility
                      filter='availability'
                      search_product_with_filter(self,filter)

               if filterMethod=='5':
                      break

def modify_product(self):
        print(f'''\n-----Modificacion de atributos-----\n Seleccione el producto a modificar:\n''')
        for idx in range(len(self.Products)):
            print(f'{idx+1} {self.Products[idx].show_atr()}')
        chose=input('Introduzca el numero del producto a modificar:')
        while not chose.isnumeric() or int(chose) not in range(1,len(self.Products)+1):
              chose=input('Invalido. Introduzca el numero del producto a modificar:')
        idx_product_to_modify=int(chose)-1
        product_to_modify=self.Products[idx_product_to_modify]
        print(f"\n Producto seleccionado: {product_to_modify.show_atr()}")
        print(f'''\n Seleccione el atributo a modificar:\n''')  
        options=['Nombre','Descripcion','Precio','Categoria','Disponibilidad']
        print_options(options)
        chose_atr=input(f'\nIntroduzca el numero del atributo que desea a modificar:')
        while not chose_atr.isnumeric() or int(chose_atr) not in range(1,6):
              chose_atr=input('Invalido. Introduzca el numero del producto a modificar:') #
        product_to_modify.modify_atr(chose_atr)
               

def del_product(self):
        print(f'''\n-----Eliminar producto-----\n Seleccione el producto a modificar:\n''')
        for idx in range(len(self.Products)):
            print(f'{idx+1} {self.Products[idx].show_atr()}')
        chose=input('Introduzca el numero del producto a eliminar:')
        while not chose.isnumeric() or int(chose) not in range(1,len(self.Products)+1):
              chose=input('Invalido. Introduzca el numero del producto a eliminar:')
        idx_product_to_del=int(chose)-1
        self.Products.pop(idx_product_to_del)
        
def product_management_module(self):
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
              print('Eliminado')


        if chose=='5': # Salir
              break

def add_customer():
        while True:
            print(f'''\n-----Agregar cliente-----\n Ingrese el tipo de cliente:\n''')
            options=['Natural','Juridico','Salir']
            print_options(options)
            chose=input('Ingrese la opcion deseada:')
            while not chose.isnumeric() or int(chose) not in range(1,len(options)+1):
                  chose=('Invalido. Ingrese la opcion deseada:')
            if chose=='3':
                  break
            print(f'''\n Ingrese los datos:\n''')
            if chose=='1':  # Natural name,kind=Natural,email,address,phoneNumber,identifierDocument=cedula
                kind='Natural'
                name=input('Introduzca el nombre y apellido del cliente:')
                while not is_naturalName(name):
                    name=input('Invalido. Introduzca el nombre y apellido del cliente:')
                email=input('Introduzca el correo gmail o hotmail del cliente:')
                while not is_email(email):
                    email=input(f'Invalido. Ej: Ejemplo2023@gmail.com \n Introduzca el correo del cliente (gmail o hotmail):')
                address=input('Introduzca la direccion del cliente:')
                while not is_address(address):
                    address=input('Invalido. Introduzca la direccion del cliente con comas y puntos (Desde 35 hasta 100 letras):')
                phoneNumber=input('Introduzca el numero de telefono del cliente con un solo punto:')
                while not is_phoneNumber(phoneNumber):
                    phoneNumber=input(f'Invalido. Ej: 0412.5557788 \n Introduzca el numero de telefono del cliente:')
                identifierDocument=input('Introduzca la cedula del cliente:')
                while not is_cedula(identifierDocument):
                    identifierDocument=input(f'Invalido. Ej: 20.982.756 \n Introduzca la cedula del cliente:')
                new_customer=Customer(name,kind,email,address,phoneNumber,identifierDocument)
                return new_customer
            
            if chose=='2':  # Legal socialReason,kind=Juridico,email,address,phoneNumber,identifierDocument=RIF
                kind='Juridico'
                socialReason=input('Introduzca la razon social del cliente con puntos y comas:')
                while not is_socialReason(socialReason):
                    socialReason=input(f'\n Invalido. Ej: PepsiCo, Inc. \n Introduzca la razon social del cliente con puntos, comas y sin numeros:')
                email=input('Introduzca el correo gmail o hotmail del cliente:')
                while not is_email(email):
                    email=input(f'\n Invalido. Ej: Ejemplo2023@gmail.com \n Introduzca el correo del cliente (gmail o hotmail):')
                address=input('Introduzca la direccion del cliente:')
                while not is_address(address):
                    address=input(f'\n Invalido. Introduzca la direccion del cliente con comas y puntos (Desde 35 hasta 100 letras):')
                phoneNumber=input('Introduzca el numero de telefono del cliente con un solo punto:')
                while not is_phoneNumber(phoneNumber):
                    phoneNumber=input(f'\n Invalido. Ej: 0412.5557788 \n Introduzca el numero de telefono del cliente:')
                rif=input('Introduzca el RIF del cliente con la J mayuscula y separado por guiones:')
                while not is_rif(rif):
                    rif=input(f'\n Invalido. Ej:# "J-29989842-2" \n Introduzca el RIF del cliente:')
                new_customer=Customer(socialReason,kind,email,address,phoneNumber,rif)
                return new_customer
        
def search_customer(self):
        while True:
               print(f'''\n -----Buscar cliente----- \n''')
               options=['Documento de identificacion (Cedula o RIF)','Correo electronico','Salir']
               print_options(options)
               filterMethod=input(f'\n Ingrese la opcion deseada:')
               while not filterMethod.isnumeric() or int(filterMethod) not in range(1,len(options)+1):
                   filterMethod=input('Invalido. Ingrese el numero de la opcion deseada:')
               if filterMethod=='1':      # Filter is id
                     id=input(f'''\n Ingrese el Documento de Identificacion (Cedula o RIF).\n Ingrese la cedula separada por puntos: Ej: "20.395.827"\n Ingrese el RIF separado por guiones (J mayus.): Ej:"J-98765434-1" \n ''') 
                     if is_cedula(id) or is_rif(id):
                           if is_cedula(id):
                                 print(f"Cedula ingresada: C.I. {id}")
                                 sum=0
                                 for customer in self.Customers:
                                       if customer.identifierDocument==id:
                                             print(customer.show_atr())
                                             sum+=1
                                 if sum==0:
                                       print('Cliente no registrado.')
                           if is_rif(id):
                             print(f"RIF ingresado: RIF: {id}")
                             sum=0
                             for customer in self.Customers:
                                 if customer.identifierDocument==id:
                                     print(customer.show_atr())
                                     sum+=1
                                 if sum==0:
                                       print(f'\nCliente no registrado.\n')
                     else:
                           print(f'\nDocumento invalido\n')
    

               if filterMethod=='2':      # Filter is email
                     email=input(f'\n Ingrese el correo electronico del cliente.\n Correo Gmail o Hotmail con al menos una mayuscula, minuscula y un numero:')
                     if is_email(email):
                           sum=0
                           for customer in self.Customers:
                                 if customer.email==email:
                                       print(customer.show_atr())
                                       sum+=1
                           if sum==0:
                                 print(f'\n Cliente no registrado.\n')
                     else: 
                           print(f'\nDocumento invalido.\n')

               if filterMethod=='3':
                      break

def modify_customer(self):      #TODO - Arreglar
        print(f'''\n-----Modificacion de atributos-----\n Seleccione el producto a modificar:\n''')
        for idx in range(len(self.Products)):
            print(f'{idx+1} {self.Products[idx].show_atr()}')
        chose=input('Introduzca el numero del producto a modificar:')
        while not chose.isnumeric() or int(chose) not in range(1,len(self.Products)+1):
              chose=input('Invalido. Introduzca el numero del producto a modificar:')
        idx_product_to_modify=int(chose)-1
        product_to_modify=self.Products[idx_product_to_modify]
        print(f"\n Producto seleccionado: {product_to_modify.show_atr()}")
        print(f'''\n Seleccione el atributo a modificar:\n''')  
        options=['Nombre','Descripcion','Precio','Categoria','Disponibilidad']
        print_options(options)
        chose_atr=input(f'\nIntroduzca el numero del atributo que desea a modificar:')
        while not chose_atr.isnumeric() or int(chose_atr) not in range(1,6):
              chose_atr=input('Invalido. Introduzca el numero del producto a modificar:') #
        product_to_modify.modify_atr(chose_atr)
               
def del_customer(self): #TODO - Arreglar
        print(f'''\n-----Eliminar producto-----\n Seleccione el producto a modificar:\n''')
        for idx in range(len(self.Products)):
            print(f'{idx+1} {self.Products[idx].show_atr()}')
        chose=input('Introduzca el numero del producto a eliminar:')
        while not chose.isnumeric() or int(chose) not in range(1,len(self.Products)+1):
              chose=input('Invalido. Introduzca el numero del producto a eliminar:')
        idx_product_to_del=int(chose)-1
        self.Products.pop(idx_product_to_del)
        print('Eliminado.')
        
def customer_management_module(self):
      while True:
        print(f'''\n-----Bienvenido al modulo de Gestion de Clientes-----\n''')
        options=['Agregar cliente.','Buscar cliente.','Modificar informacion de un cliente.','Eliminar cliente.','Salir.']
        print_options(options)
        chose=input('''\nIngrese la opcion deseada:''')
        while not chose.isnumeric() or int(chose) not in range(1,len(options)+1):
            chose=input('''\nOpcion invalida. Ingrese la opcion deseada:\nIngrese 0 Para salir
                ''')
            if chose=='0':
                break
        if chose=='1': # Agregar cliente
               new_customer=add_customer()
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

def generate_bill():
      pass

def register_sale(self): #date,saleNumber, customer, productsAmount #Nueva idea , paymentMethod, shippingMethod,totalAmount
      pass

def search_sale(self):
      pass

def register_pay(self):
      pass

def search_pay(self):
      pass

def register_shipping(self):
      pass

def search_shipping(self):
      pass

