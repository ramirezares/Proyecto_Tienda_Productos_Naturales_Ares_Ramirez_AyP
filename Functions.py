from Date import Date
from Product import Product
from Natural import Natural
from Legal import Legal
from Pay import Pay
from Delivery import Delivery

from Validations import *

#Generales

def print_options(options:list):  
        for i in range(len(options)):
                    print(f'{i+1}: {options[i]}')

def calculate_deadline(saleTime,today:Date,amount_of_days:int):
        if saleTime=="Pago de contado":
              return None
        else:
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
        
def set_date():
      year=input('Ingrese el año:')
      while not is_int(year) or not len(year)==4:
            year=input('Año invalido. Ingrese el año:')
      
      month=input('Ingrese el numero del mes:')
      while not is_int(month) or not len(month)>=1 or not len(month)<=2:
            month=input('Mes invalido. Ingrese el numero del mes:')
      
      day=input('Ingrese el numero del dia:')
      while not is_int(day) or not len(day)>=1 or not len(day)<=2:
            day=input('Dia invalido. Ingrese el numero del dia:')
      date=Date(int(day),int(month),int(year))
      
      while not is_date(Date(int(day),int(month),int(year))):
            print(f'\n Datos invalidos. Por favor revise e ingrese nuevamente.\n')      
            year=input('Ingrese el año:')
            while not is_int(year) or not len(year)==4:
                  year=input('Año invalido. Ingrese el año:')
            
            month=input('Ingrese el numero del mes:')
            while not is_int(month) or not len(month)>=1 or not len(month)<=2:
                  month=input('Mes invalido. Ingrese el numero del mes:')
            
            day=input('Ingrese el numero del dia:')
            while not is_int(day) or not len(day)>=1 or not len(day)<=2:
                  day=input('Ingrese el numero del dia:')
      date=Date(int(day),int(month),int(year))
      print(f'\n Fecha ingresada correctamente. \n')
      return date

# Product Management

def add_product():
        print(f'\n -----Agregar producto-----\n Ingrese los datos:')
        name=input('Ingrese el nombre del producto:')
        while not is_productName(name):
                name=input('Invalido. Ingrese el nombre del producto:')
        description=input('Ingrese la descripcion del producto:')
        while not is_description(description):
                description=input('Invalido. Ingrese la descripcion del producto con comas o puntos:')
        price=input('Ingrese el precio del producto:')
        while not is_price(price):
                price=input('Invalido. Ingrese el precio del producto:')
        category=input('Ingrese la categoria del producto:')
        while not is_category(category):
                category=input('Invalido. Ingrese la categoria del producto:')
        stock=input('Ingrese la cantidad del producto:')
        while not is_availability(stock):
                stock=input('Invalido. Ingrese la cantidad del producto:')
        availability=int(stock)
        new_product=Product(name,description,float(price),category,availability)
        return new_product

def search_product_with_filter(self,filter:str):
    if filter=='category':
          matchedAlternatives=[]
          for dic in self.Products:
            if dic.category not in matchedAlternatives:
                  matchedAlternatives.append(dic.category)
          matchedAlternatives.sort()
          print(f'\nOpciones encontradas con el filtro:')
          print_options(matchedAlternatives)
          chose=input(f'\nSeleccione la opcion deseada:')
          while not chose.isnumeric() or int(chose) not in range(1,len(matchedAlternatives)+1):
              chose=input(f'\n Opcion invalida. Ingrese la opcion deseada:')
          categorySelected=matchedAlternatives[int(chose)-1]
          print(f'\n Productos encontrados:')
          for dic in self.Products:
                 if dic.category==categorySelected:
                       print(dic.show_atr())
    if filter=='price':
          matchedAlternatives=[]
          for dic in self.Products:
            if dic.price not in matchedAlternatives:
                  matchedAlternatives.append(dic.price)
          matchedAlternatives.sort()
          print(f'\nOpciones encontradas con el filtro(Numero opcion: Precio):')
          print(f'\n')
          print_options(matchedAlternatives)
          chose=input(f'\nSeleccione la opcion deseada:')
          while not chose.isnumeric() or int(chose) not in range(1,len(matchedAlternatives)+1):
              chose=input(f'\nOpcion invalida. Ingrese la opcion deseada:')
          priceSelected=matchedAlternatives[int(chose)-1]
          print(f'\n Productos encontrados:')
          for dic in self.Products:
                 if dic.price==priceSelected:
                       print(dic.show_atr())
    if filter=='availability':
          matchedAlternatives=[]
          for dic in self.Products:
            if dic.availability not in matchedAlternatives:
                  matchedAlternatives.append(dic.availability)
          matchedAlternatives.sort()
          print(f'\nOpciones encontradas con el filtro:')
          print(f'\n')
          print_options(matchedAlternatives)
          chose=input(f'\nSeleccione la opcion deseada:')
          while not chose.isnumeric() or int(chose) not in range(1,len(matchedAlternatives)+1):
              chose=input(f'\n Opcion invalida. Ingrese la opcion deseada:')
          availabilitySelected=matchedAlternatives[int(chose)-1]
          print(f'\n Productos encontrados:')
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
                      name=input(f'\nIntroduzca el nombre a buscar:')
                      while not is_productName(name):
                             name=input(f'\nInvalido. Introduzca el nombre a buscar:')    
                      sum=0
                      print(f'\n Productos encontrados:')
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
        while True:
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
            options=['Nombre','Descripcion','Precio','Categoria','Disponibilidad','Salir']
            print_options(options)
            chose_atr=input(f'\nIntroduzca el numero del atributo que desea a modificar:')
            while not chose_atr.isnumeric() or int(chose_atr) not in range(1,len(options)+1):
                  chose_atr=input('Invalido. Introduzca el numero del producto a modificar:') 
            if chose_atr=='6':
                  break
            else:
                  product_to_modify.modify_atr(chose_atr)
                  break
               
def del_product(self):
        if len(self.Products)==0:
              print('No hay productos registrados.')
        if len(self.Products)>0:  
            print(f'''\n-----Eliminar producto-----\n Seleccione el producto a eliminar:\n''')
            for idx in range(len(self.Products)):
                print(f'{idx+1} {self.Products[idx].show_atr()}')
            chose=input('Introduzca el numero del producto a eliminar:')
            while not chose.isnumeric() or int(chose) not in range(1,len(self.Products)+1):
                  chose=input('Invalido. Introduzca el numero del producto a eliminar:')
            idx_product_to_del=int(chose)-1
            self.Products.pop(idx_product_to_del)

# Customer Management

def add_customer(self):
        while True:
            print(f'\n-----Agregar cliente-----\n \nIngrese el tipo de cliente:\n')
            options=['Natural','Juridico','Salir']
            print_options(options)
            chose=input('Ingrese la opcion deseada:')
            while not is_int(chose) or int(chose) not in range(1,len(options)+1):
                  chose=input('Invalido. Ingrese la opcion deseada:')
            if chose=='3':
                  break
            print(f'''\n Ingrese los datos:''')
            if chose=='1':  # Natural name,kind=Natural,email,address,phoneNumber,identifierDocument=cedula
                kind='Natural'
                name=input(f'\n Introduzca el nombre y apellido del cliente:')
                while not is_naturalName(name):
                    name=input(f'\n Invalido. Introduzca el nombre y apellido del cliente sin numeros, con un solo espacio:')
                email=input(f'\n Introduzca el correo del cliente (gmail o hotmail, al menos una minuscula, mayuscula y un numero):')
                while not is_email(email):
                    email=input(f'Invalido. Ej: Ejemplo2023@gmail.com \n Introduzca el correo del cliente (gmail o hotmail):')
                address=input(f'\n Introduzca la direccion del cliente:')
                while not is_address(address):
                    address=input('Invalido. Introduzca la direccion del cliente con comas y puntos (35-100 letras) Ej: Urb. Valle Arriba, Calle 2, Galpon 1. Guatire. Miranda:')
                phoneNumber=input(f'\n Introduzca el numero de telefono del cliente con un solo punto:')
                while not is_phoneNumber(phoneNumber):
                    phoneNumber=input(f'Invalido. Ej: 0412.5557788 \n Introduzca el numero de telefono del cliente:')
                identifierDocument=input(f'\n Introduzca la cedula del cliente separada por dos puntos:')
                while not is_cedula(identifierDocument):
                    identifierDocument=input(f'Cedula invalida. Ej: 20.982.756 \n Introduzca la cedula del cliente:')
                new_customer=Natural(name,kind,email,address,phoneNumber,identifierDocument)
                
                for customer in self.Customers:
                      if customer.identifierDocument==new_customer.identifierDocument:
                            print(f'\nCedula ya registrada.')
                            return None
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
                    address=input(f'\n Invalido. Introduzca la direccion del cliente con comas y puntos (Desde 35 hasta 100 letras) Ej: Urb. Valle Arriba, Calle 2, Galpon 1. Guatire. Miranda:')
                phoneNumber=input('Introduzca el numero de telefono del cliente con un solo punto:')
                while not is_phoneNumber(phoneNumber):
                    phoneNumber=input(f'\n Invalido. Ej: 0412.5557788 \n Introduzca el numero de telefono del cliente:')
                rif=input('Introduzca el RIF del cliente con la J mayuscula y separado por guiones:')
                while not is_rif(rif):
                    rif=input(f'\n Invalido o ya registrado. Ej: "J-29989842-2" \n Introduzca el RIF del cliente:')
                new_customer=Legal(socialReason,kind,email,address,phoneNumber,rif)
                for customer in self.Customers:
                      if customer.identifierDocument==new_customer.identifierDocument:
                            print(f'\nRIF ya registrado.')
                            return None
                return new_customer
        
def search_customer(self):
        while True:
               if len(self.Customers)>0:
                  print(f'\n -----Buscar cliente----- \n')
                  options=['Documento de identificacion (Cedula o RIF)','Correo electronico','Salir']
                  print_options(options)
                  filterMethod=input(f'\n Ingrese la opcion deseada:')
                  while not filterMethod.isnumeric() or int(filterMethod) not in range(1,len(options)+1):
                      filterMethod=input('Invalido. Ingrese el numero de la opcion deseada:')
                  if filterMethod=='1':      # Filter is id
                        id=input(f'''\n Ingrese el Documento de Identificacion (Cedula o RIF).\n Si es cedula, ingrese la cedula separada por puntos: Ej: "20.395.827"\n Si es RIF, ingrese el RIF separado por guiones (J mayus.): Ej:"J-98765434-1" \n Ingrese la Cedula o el RIF:''') 
                        if is_cedula(id) or is_rif(id):
                              if is_cedula(id):
                                    print(f"\n Cedula ingresada: C.I. {id}")
                                    sum=0
                                    for customer in self.Customers:
                                          if customer.identifierDocument==id:
                                                print(f'\n Cliente encontrado: {customer.show_atr()}')
                                                sum+=1
                                    if sum==0:
                                          print(f'\n Cliente no registrado.')
                              if is_rif(id):
                                    print(f"\n RIF ingresado: RIF: {id}")
                                    sum=0
                                    for customer in self.Customers:
                                          if customer.identifierDocument==id:
                                                print(f'\n Cliente encontrado: {customer.show_atr()}')
                                                sum+=1
                                    if sum==0:
                                          print(f'\nCliente no registrado.\n')
                        else:
                              print(f'\nDocumento invalido\n')

                  if filterMethod=='2':      # Filter is email
                        email=input(f'\n Ingrese el correo electronico del cliente.\n Correo Gmail o Hotmail con al menos una mayuscula, minuscula y un numero:')
                        if is_email(email):
                              print(f"\n Correo ingresado: {email}")
                              sum=0
                              for customer in self.Customers:
                                    if customer.email==email:
                                          print(f'\n Cliente encontrado: {customer.show_atr()}')
                                          sum+=1
                              if sum==0:
                                    print(f'\n Cliente no registrado.\n')
                        else: 
                              print(f'\n Correo invalido.\n')

                  if filterMethod=='3':
                         break
               else:
                     print(f'\nNo hay clientes registrados.')
                     break

def chosing_atr(options:list,):
      print_options(options)
      chose_atr=input(f'\n Introduzca el numero del atributo que desea a modificar:')
      while not chose_atr.isnumeric() or int(chose_atr) not in range(1,len(options)+1):
            chose_atr=input('Invalido. Introduzca el numero del producto a modificar:') 
      return chose_atr

def modify_customer(self):  
        while True:
            if len(self.Customers)>0:
                  print(f'''\n-----Modificacion de atributos-----\n''')
                  id=input(f'''Introduzca la cedula o RIF del cliente.\nSi es cedula ingresar separada con puntos. Ej: 20.952.864\nSi es RIF ingresar con J mayuscula y separada pro guiones. Ej: J-29989842-2.\n Ingresa la cedula o RIF:''')
                  if is_cedula(id) or is_rif(id):
                      customer_to_modify=None
                      aux=0
                      for i in range(len(self.Customers)):
                          if self.Customers[i].identifierDocument==id:
                                customer_to_modify=self.Customers[i]
                                aux+=1
                      if aux==0:
                            print('Cliente no encontrado')
                            break

                      if type(customer_to_modify)==Natural or type(customer_to_modify)==Legal:
                            print(f"\n Cliente seleccionado: {customer_to_modify.show_atr()}")
                            print(f'''\n Seleccione el atributo a modificar.\n''')  

                            if customer_to_modify.kind=='Natural':                # Natural: name email address phoneNumber identifierDocument
                                  options=['Nombre','Correo','Direccion','Numero de telefono','Cedula','Salir']
                                  chose_atr=chosing_atr(options)
                                  if chose_atr=='6':
                                        break
                                  else:
                                        customer_to_modify.modify_atr(chose_atr)
                                        break

                            if customer_to_modify.kind=='Juridico':    # Legal: socialReason email address phoneNumber RIF
                                  options=['Razon social','Correo','Direccion','Numero de telefono','RIF','Salir']
                                  chose_atr=chosing_atr(options)
                                  if chose_atr=='6':
                                        break
                                  else:
                                        customer_to_modify.modify_atr(chose_atr)
                                        break
                  else:
                        print('Invalido.')
            else:
                  print(f'\nNo hay clientes registrados.')
                  break

def del_customer(self):
        if len(self.Customers)==0:
              print(f'\nNo hay clientes registrados.')
        if len(self.Customers)>0:          
            while True:
                  print(f'''\n-----Eliminar cliente-----\n Seleccione el cliente a eliminar:\n''')
                  for idx in range(len(self.Customers)):
                      print(f'{idx+1} {self.Customers[idx].show_atr()}')
                  chose=input('Introduzca el numero del cliente a eliminar o 0 para cancelar:')
                  if chose=="0":
                        break
                  while not chose.isnumeric() or int(chose) not in range(1,len(self.Customers)+1):
                        chose=input('Invalido. Introduzca el numero del cliente a eliminar:')
                  idx_product_to_del=int(chose)-1
                  self.Customers.pop(idx_product_to_del)
                  print('Eliminado.')
                  break

# Sales management

def generate_bill(self):
      if len(self.Sales)>0:
            print(f'\n ------Generar factura------\n Seleccione la venta:\n')
            for sale in self.Sales:
                  print(f'{sale.saleNumber} {sale.customer.name} {sale.customer.identifierDocument} {sale.breakdown}')
            chose=input(f'\nIngrese la venta deseada:')
            while not is_int(chose) or int(chose) not in range(1,len(self.Sales)+1):
                  chose=input(f'\n Invalido. Ingrese el numero la venta deseada:')
            sale=self.Sales[int(chose)-1]
            print(sale.show_atr())        # Falta un comando para que mande a imprimirlo en una impresora JAJAJAJ
            
      else:
            print(f'\nNo hay ventas registradas')

def generate_final_bill(sale):
      print(sale.show_atr())      

def calculate_saleNumber(self):
      if len(self.Sales)==0:
            saleNumber=1
      else:
            registered_sales=len(self.Sales)
            saleNumber=registered_sales+1
      saleNumber_inStr=str(saleNumber)
      return saleNumber_inStr

def define_selected_customer(self,id):
      selected_customer=None
      for c in self.Customers:
            if c.identifierDocument==id:
                  selected_customer=c
      return selected_customer

def select_naturalCustomer(self):
      while True:
            print(f'\n-----Seleccion de cliente-----\n')
            options=['Buscar cliente.','Registrar cliente.']
            print_options(options)
            chose=input(f'\nIngrese la opcion deseada:')
            while not is_int(chose) or int(chose) not in range(1,len(options)+1):
                  chose=input('Invalido. Ingrese la opcion deseada:')
            if chose=='1':
                  if len(self.Customers)>0:
                        id=input(f'\nIntroduzca la cedula del cliente: ')
                        while not is_cedula(id):
                              id=input(f'\n Invalido. Introduzca la cedula separada por puntos: Ej: "20.395.827"\n Ingrese la Cedula del cliente:')
                        selected_customer=define_selected_customer(self,id)
                        if type(selected_customer)==Natural:
                              print(f"\nCliente seleccionado: {selected_customer.show_atr()}")
                              return selected_customer
                        else:
                              print(f'\nCliente no encontrado.')
                              continue
                  else:
                      print(f'\n No hay clientes registrados. Por favor registre un cliente antes de registrar una venta.')
                      continue
            if chose=='2':
                  new_customer=add_customer(self)
                  self.Customers.append(new_customer)
                  print(f'\n Registrado. \n')

def select_legalCustomer(self):
      while True:
            print(f'\n-----Seleccion de cliente-----\n')
            options=['Buscar cliente.','Registrar cliente.']
            print_options(options)
            chose=input(f'\nIngrese la opcion deseada:')
            while not is_int(chose) or int(chose) not in range(1,len(options)+1):
                  chose=input('Invalido. Ingrese la opcion deseada:')
            if chose=='1':
                  if len(self.Customers)>0: 
                        id=input(f'\nIntroduzca el RIF del cliente: ')
                        while not is_rif(id):
                              id=input(f'\n Invalido. Introduzca el RIF separado por guiones y con la J mayuscula: Ej: "J-29989842-2"\n Ingrese el RIF del cliente:')
                        selected_customer=define_selected_customer(self,id)
                        if type(selected_customer)==Legal:
                              print(f"\nCliente seleccionado: {selected_customer.show_atr()}")
                              return selected_customer
                        else:
                              print(f'\nCliente no encontrado.')
                              continue
                  else:
                      print(f'\n No hay clientes registrados. Por favor registre un cliente antes de registrar una venta.')
                      continue
            if chose=='2':
                  new_customer=add_customer(self)
                  self.Customers.append(new_customer)
                  print(f'\n Registrado. \n')
      
def select_products(self):
      selected_products=[]
      while True:
            print(f'\n-----Seleccion de productos-----\n')
            if len(selected_products)>0:
                  print(f'\n --Carro de compras --\n')
                  enumerateAux=0
                  for p in selected_products:
                        enumerateAux+=1
                        print(f'{enumerateAux}. {p}')
                  print(f'\n----------------------\n')
            aux=0
            for i in range(len(self.Products)):
                  if self.Products[i].availability>0:
                        aux+=1
                        print(f'{i+1} {self.Products[i].show_atr()}')
            if aux>0:
                  chose=input('Ingrese el numero del producto que desea comprar:')
                  while not is_int(chose) or int(chose) not in range(1,len(self.Products)+1):
                        chose=input('Invalido. Ingrese el numero del producto que desea comprar:')
                  product=self.Products[int(chose)-1]
                  print(f'\n Producto seleccionado: {product.show_atr()}')

                  qty=input("Ingrese la cantidad deseada:")       
                  while not is_int(qty) or not int(qty)<=product.availability:
                        qty=input("Invalido. Ingrese la cantidad deseada:")
                  product_i={"name":product.name,"price":product.price,"amount":int(qty),"subtotal":int(product.price)*int(qty)}
                  
                  new_stock=self.Products[int(chose)-1].availability-int(qty) #Resta cantidad de productos vendidos del almacen
                  self.Products[int(chose)-1].availability=new_stock
                  
                  selected_products.append(product_i)
                  decition=input(f'\n¿Desea continuar comprando? (y/n):')               
                  options=['y','n']
                  while decition not in options:
                        decition=input('Opcion invalida. ¿Desea continuar comprando? (y/n):')
                  if decition=='y':
                        continue
                  elif decition=='n':
                        return selected_products
            else:
                  return selected_products
            
def select_paymentMethod():
      print(f'\n-----Seleccion del metodo de Pago-----\n')
      options=['Transferencia (Bs)','Pago Movil (Bs)','Zelle ($)','Cash ($)']
      print_options(options)
      chose=input(f'\nIngrese el numero de la opcion deseada:')
      while not is_int(chose) or int(chose)-1 not in range(len(options)):
            chose=input(f'\nInvalido. Ingrese el numero de la opcion deseada:')
      paymentMethod=options[int(chose)-1]
      return paymentMethod
            
def select_shippingMethod():
      print(f'\n-----Seleccion del metodo de envio-----\n')
      options=['Envio de paquetes','Delivery']
      print_options(options)
      chose=input(f'\nIngrese el numero de la opcion deseada:')
      while not is_int(chose) or int(chose)-1 not in range(len(options)):
            chose=input(f'\nInvalido. Ingrese el numero de la opcion deseada:')
      shippingMethod=options[int(chose)-1]
      return shippingMethod

def build_Products_breakdown(products:list):
      Products_breakdown=[]
      for p in products:
            name=p['name']
            price=p['price']
            amount=p['amount']
            subtotal=p['subtotal']
            line=f'{name}   Precio unidad:{price}.   Cantidad:{amount}  = {subtotal}\n'
            Products_breakdown.append(line)
      return Products_breakdown

def calculate_subtotal(products):
      subtotal=0
      for dic in products:
            value=int(dic["subtotal"])
            subtotal+=value
      return subtotal

def calculate_SaletotalAmount(subtotal,IVA,IGFT):
      Total=0
      IVA_for_sale=subtotal*int(IVA[0:2])/100
      IGTF_for_sale=subtotal*int(IGFT[0])/100
      Total=subtotal+IVA_for_sale+IGTF_for_sale             
      return Total

def calculate_LegalSaletotalAmount(subtotal,discount,IVA,IGFT,val):
      if val==True:
            Total=0
            Discount_for_sale=subtotal*int(discount[0])/100
            subtotal-=Discount_for_sale
            IVA_for_sale=(subtotal*int(IVA[0:2]))/100
            IGTF_for_sale=(subtotal*int(IGFT[0]))/100
            Total+=subtotal+IVA_for_sale+IGTF_for_sale 
      else:
            Total=0
            Discount_for_sale=subtotal*int(discount[0])/100
            subtotal-=Discount_for_sale
            IVA_for_sale=(subtotal*int(IVA[0:2]))/100
            Total+=subtotal+IVA_for_sale 
      return Total

def build_SaletotalAmount_breakdown(paymentMethod,products):
      if '$' in paymentMethod:
            items_for_breakdown=['Subtotal','IVA','IGTF','Total']
            Breakdown={}
            subtotal=calculate_subtotal(products)
            IVA="16%"
            IGTF="3%"
            Total=calculate_SaletotalAmount(subtotal,IVA,IGTF)
            values=[subtotal,IVA,IGTF,Total]
            i=0
            for item in items_for_breakdown:
                  Breakdown[f'{item}']=values[i]
                  i+=1
      else:
            items_for_breakdown=['Subtotal','IVA','IGTF','Total']
            Breakdown={}
            subtotal=calculate_subtotal(products)
            IVA="16%"
            IGTF="0%"
            Total=calculate_SaletotalAmount(subtotal,IVA,IGTF)
            values=[subtotal,IVA,IGTF,Total]
            i=0
            for item in items_for_breakdown:
                  Breakdown[f'{item}']=values[i]
                  i+=1
      return Breakdown

def calculate_discount(saleTime):
      if saleTime=='Pago de contado':
            discount=5
      else:
            discount=0
      return discount

def build_LegalSaletotalAmount_breakdown(paymentMethod,discount,products):
      if '$' in paymentMethod:
            items_for_breakdown=['Subtotal','Discount','IVA','IGTF','Total']
            Breakdown={}
            subtotal=calculate_subtotal(products)
            Discount=f"{discount}%"
            IVA="16%"
            IGTF="3%"
            Total=calculate_LegalSaletotalAmount(subtotal,Discount,IVA,IGTF,True)
            values=[subtotal,Discount,IVA,IGTF,Total]
            i=0
            for item in items_for_breakdown:
                  Breakdown[f'{item}']=values[i]
                  i+=1
      else:
            items_for_breakdown=['Subtotal','Discount','IVA','IGTF','Total']
            Breakdown={}
            subtotal=calculate_subtotal(products)
            Discount=f"{discount}%"
            IVA="16%"
            IGTF="0%"
            Total=calculate_LegalSaletotalAmount(subtotal,Discount,IVA,IGTF,False)
            values=[subtotal,Discount,IVA,IGTF,Total]
            i=0
            for item in items_for_breakdown:
                  Breakdown[f'{item}']=values[i]
                  i+=1
      return Breakdown 

def search_sale(self):
      while True:
            if len(self.Sales)>0:
                  print(f'''\n -----Buscar Venta----- \n''')
                  options=['Por cliente.','Por fecha.','Por monto total.','Salir.']
                  print_options(options)
                  filterMethod=input(f'\n Ingrese la opcion deseada:')
                  while not filterMethod.isnumeric() or int(filterMethod) not in range(1,len(options)+1):
                      filterMethod=input('Invalido. Ingrese el numero de la opcion deseada:')
                  
                  if filterMethod=='1':      # Filter is Customer.
                        print(f'''\n -Buscar por cliente- \n''')
                        options=['Natural','Juridico']
                        print_options(options)
                        chose=input(f'\nIngrese la opcion deseada:')
                        while not is_int(chose) or int(chose) not in range(1,len(options)+1):
                              chose=input(f'\nInvalido. Ingrese la opcion deseada:')
                        if chose=='1':
                              id=input(f'\nIngrese la cedula del cliente:')
                              while not is_cedula(id):
                                    id=input(f'\n Invalido. Introduzca la cedula separada por puntos: Ej: "20.395.827"\n Ingrese la Cedula del cliente:')
                        else:
                              id=input(f'\nIngrese el RIF del cliente:')
                              while not is_rif(id):
                                    id=input(f'\n Invalido. Introduzca el RIF separado por guiones y con la J mayuscula. Ej: "J-29989842-2"\n Ingrese el RIF del cliente:')
                        print(f'\nVentas encontradas:')
                        aux=0
                        for sale in self.Sales:
                              if sale.customer.identifierDocument==id:
                                    aux+=1
                                    print(f'{aux} {sale.show_atr()}')
                        if aux==0:
                              print(f'\nSin resultados')
                  
                  if filterMethod=='2':      # Filter is Date
                        print(f'''\n -Buscar por fecha- \n''')
                        date_searched=set_date()
                        print(f'\nVentas encontradas:')
                        aux=0
                        for s in self.Sales:
                              if s.date.day==date_searched.day and s.date.month==date_searched.month and s.date.year==date_searched.year:
                                    aux+=1
                                    print(f'{aux} {s.show_atr()}')
                        if aux==0:
                              print(f'\nSin resultados')

                  if filterMethod=='3':      # Filter is TotalAmount
                        print(f'''\n -Buscar por monto total- \n''')
                        options=['Buscar por monto introducido','Buscar por montos de ventas realizadas']
                        print_options(options)
                        chose=input(f'\nIngrese la opcion deseada:')
                        while not is_int(chose) or int(chose) not in range(1,len(options)+1):
                              chose=input(f'\nInvalido. Ingrese la opcion deseada:')
                        if chose=='1':
                              totalAmount=input("Ingrese el monto total exacto a buscar:")
                              while not is_float(totalAmount) and not is_float(totalAmount):
                                    totalAmount=input("Invalido. Ingrese el monto total exacto a buscar:")
                              print(f'\nVentas encontradas:')
                              aux=0
                              for s in self.Sales:
                                    if s.breakdown['Total']==float(totalAmount):
                                          aux+=1
                                          print(f'{aux}. {s.show_atr()}')
                              if aux==0:
                                    print(f'\nSin resultados')
                        else:
                              matched=[]
                              for s in self.Sales:
                                    if s.breakdown['Total'] not in matched:
                                          matched.append(s.breakdown['Total'])
                              matched.sort()
                              print(f'\nOpciones encontradas:')
                              print_options(matched)
                              chose=input(f'\nSeleccione la opcion deseada:')
                              while not chose.isnumeric() or int(chose) not in range(1,len(matched)+1):
                                    chose=input(f'\n Opcion invalida. Ingrese la opcion deseada:')
                              optionSelected=matched[int(chose)-1]
                              print(f'\n Ventas encontradas:')
                              for s in self.Sales:
                                    if s.breakdown['Total']==optionSelected:
                                          print(s.show_atr())
                         
                  if filterMethod=='4':      # Salir
                        break
            else:
                  print(f'\n No hay ventas registradas')
                  break

# Payment Management

def get_paymentCurrency(sale):
      if sale.paymentMethod=='Transferencia (Bs)' or sale.paymentMethod=='Pago Movil (Bs)':
            return 'Bolivares Bs.'
      else:
            return 'Dolares USD $.'

def calculate_payNumber(self):
      if len(self.payments)==0:
            saleNumber=1
      else:
            registered_sales=len(self.Sales)
            saleNumber=registered_sales+1
      saleNumber_inStr=str(saleNumber)
      return saleNumber_inStr

def search_pay(self):
      while True:
            if len(self.Payments)>0:
                  print(f'''\n -----Buscar pago----- \n''')
                  options=['Por cliente.','Por fecha.','Por tipo de pago.','Por moneda de pago','Salir.']
                  print_options(options)
                  filterMethod=input(f'\n Ingrese la opcion deseada:')
                  while not filterMethod.isnumeric() or int(filterMethod) not in range(1,len(options)+1):
                      filterMethod=input('Invalido. Ingrese el numero de la opcion deseada:')
                  
                  if filterMethod=='1':      # Filter is Customer.
                        print(f'''\n -Buscar por cliente- \n''')
                        options=['Natural','Juridico']
                        print_options(options)
                        chose=input(f'\nIngrese la opcion deseada:')
                        while not is_int(chose) or int(chose) not in range(1,len(options)+1):
                              chose=input(f'\nInvalido. Ingrese la opcion deseada:')
                        if chose=='1':
                              id=input(f'\nIngrese la cedula del cliente:')
                              while not is_cedula(id):
                                    id=input(f'\n Invalido. Introduzca la cedula separada por puntos: Ej: "20.395.827"\n Ingrese la Cedula del cliente:')
                        else:
                              id=input(f'\nIngrese el RIF del cliente:')
                              while not is_rif(id):
                                    id=input(f'\n Invalido. Introduzca el RIF separado por guiones y con la J mayuscula. Ej: "J-29989842-2"\n Ingrese el RIF del cliente:')
                        print(f'\nPagos encontrados:')
                        aux=0
                        for pay in self.Payments:
                              if pay.customer.identifierDocument==id:
                                    aux+=1
                                    print(f'{aux} {pay.show_atr()}')
                        if aux==0:
                              print(f'\nSin resultados')
                  
                  if filterMethod=='2':      # Filter is Date
                        print(f'''\n -Buscar por fecha- \n''')
                        date_searched=set_date()
                        print(f'\n Pagos encontrados:')
                        aux=0
                        for p in self.Payments:
                              if p.date.day==date_searched.day and p.date.month==date_searched.month and p.date.year==date_searched.year:
                                    aux+=1
                                    print(f'{aux} {p.show_atr()}')
                        if aux==0:
                              print(f'\nSin resultados')

                  if filterMethod=='3':      # Filter es tipo de pago 
                        print(f'''\n -Buscar por monto total- \n''')
                        options=['Transferencia (Bs)','Pago Movil (Bs)','Zelle ($)','Cash ($)']
                        print_options(options)
                        chose=input(f'\nIngrese la opcion deseada:')
                        while not is_int(chose) or int(chose) not in range(1,len(options)+1):
                              chose=input(f'\nInvalido. Ingrese la opcion deseada:')
                        if chose=='1':
                              payKind='Transferencia (Bs)'
                        elif chose=='2':
                              payKind='Pago Movil (Bs)'
                        elif chose=='3':
                              payKind='Zelle ($)'
                        else:
                              payKind='Cash ($)'

                        print(f'\nPagos encontrados:')
                        aux=0
                        for pay in self.Payments:
                              if pay.paymentType==payKind:
                                    aux+=1
                                    print(f'{aux} {pay.show_atr()}')
                        if aux==0:
                              print(f'\nSin resultados')
                        
                  if filterMethod=='4':      # Filter es moneda de pago
                        print(f'''\n -Buscar por monto total- \n''')
                        options=['Bolivares Bs.','Dolares USD $.']
                        print_options(options)
                        chose=input(f'\nIngrese la opcion deseada:')
                        while not is_int(chose) or int(chose) not in range(1,len(options)+1):
                              chose=input(f'\nInvalido. Ingrese la opcion deseada:')
                        if chose=='1':
                              payCurrency_Searched='Bolivares Bs.'
                        else:
                              payCurrency_Searched='Dolares USD $.'
                        print(f'\nPagos encontrados:')
                        aux=0
                        for pay in self.Payments:
                              if pay.paymentCurrency==payCurrency_Searched:
                                    aux+=1
                                    print(f'{aux} {pay.show_atr()}')
                        if aux==0:
                              print(f'\nSin resultados')
                        
                  if filterMethod=='5':      # Salir
                        break
            else:
                  print(f'\n No hay pagos registrados')
                  break

# Shipping Management

def search_and_verf_pay(self,sale):
      if len(self.Payments)>0:
            for pay in self.Payments:
                  if sale.saleNumber in pay.payNumber:
                        return True
            return False
      else: 
            return False

def calculate_shippingCost(sale):
      ShippingServices=[{'Nombre':'MRW',
                         'Tipo de envio':'Envio de paquetes',
                         "Envio de larga distancia":"700",
                         "Envio de corta distancia":"420"
                         },
                         {'Nombre':'Zoom',
                          'Tipo de envio':'Envio de paquetes',
                          "Envio de larga distancia":"700",
                          "Envio de corta distancia":"420"
                          },
                          {'Nombre':'Yummy',
                           'Tipo de envio':'Delivery',
                           "Envio rapido":"140"
                           },
                          {'Nombre':'PedidosYa',
                           'Tipo de envio':'Delivery',
                           "Envio rapido":"140"
                           }
                           ]
      if sale.shippingMethod=='Envio de paquetes':
            options=[]
            for dic in ShippingServices:
                  if dic['Tipo de envio']=='Envio de paquetes':
                        options.append(dic['Nombre'])
            print(f'\n-Selecion de la compañia de envios-\nSeleccione los datos deseados')
            print_options(options)
            chose=input(f'\nIngrese la opcion deseada:')
            while not is_int(chose) or int(chose) not in range(1,len(options)+1):
                  chose=input(f'\nInvalido. Ingrese el numero de la opcion deseada:')
            shippingCompany=options[int(chose)-1]
            print(f'\n')
            distanceOptions=['Envio de corta distancia','Envio de larga distancia']
            print_options(distanceOptions)
            distance=input(f'\nIngrese el numero de la opcion:')
            while not is_int(distance) or int(distance) not in range(1,len(distanceOptions)+1):
                  chose=input(f'\nInvalido. Ingrese el numero de la opcion deseada:')
            shippingDistance=distanceOptions[int(chose)-1]
            shippingCost=0
            for dic in ShippingServices:
                  if dic['Nombre']==shippingCompany:
                        shippingCost=dic[f'{shippingDistance}']
            return int(shippingCost)

      elif sale.shippingMethod=='Delivery':
            options=[]
            for dic in ShippingServices:
                  if dic['Tipo de envio']=='Delivery':
                        options.append(dic['Nombre'])
            print(f'\n-Selecion de la compañia de envios-\nSeleccione los datos deseados')
            print_options(options)
            chose=input(f'\nIngrese la opcion deseada:')
            while not is_int(chose) or int(chose) not in range(1,len(options)+1):
                  chose=input(f'\nInvalido. Ingrese el numero de la opcion deseada:')
            shippingCompany=options[int(chose)-1]
            print(f'\n')
            distanceOptions=['Envio rapido']
            print_options(distanceOptions)
            distance=input(f'\nIngrese el numero de la opcion:')
            while not is_int(distance) or int(distance) not in range(1,len(distanceOptions)+1):
                  distance=input(f'\nInvalido. Ingrese el numero de la opcion deseada:')
            shippingDistance=distanceOptions[int(distance)-1]
            shippingCost=0
            for dic in ShippingServices:
                  if dic['Nombre']==shippingCompany:
                        shippingCost=dic[f'{shippingDistance}']
            return int(shippingCost)
      else:
            return 0.0
      
def register_delivery():
      print(f'\n-Registro de datos del delivery-\n Ingrese los datos del delivery.')
      
      name=input(f'\n Introduzca el nombre y apellido del cliente:')
      while not is_naturalName(name):
            name=input(f'\n Invalido. Introduzca el nombre y apellido del cliente sin numeros, con un solo espacio:')
      identifierDocument=input(f'\n Introduzca la cedula del cliente separada por dos puntos:')
      while not is_cedula(identifierDocument):
            identifierDocument=input(f'Invalida o ya registrada. Ej: 20.982.756 \n Introduzca la cedula del cliente:') 
      phoneNumber=input(f'\n Introduzca el numero de telefono del cliente con un solo punto:')
      while not is_phoneNumber(phoneNumber):
            phoneNumber=input(f'Invalido. Ej: 0412.5557788 \n Introduzca el numero de telefono del cliente:')
      delivery=Delivery(name,identifierDocument,phoneNumber)
      
      return delivery

def search_shipping(self):
      while True:
            if len(self.Shipped)>0:
                  print(f'''\n -----Buscar envio----- \n''')
                  options=['Por cliente.','Por fecha.','Salir.']
                  print_options(options)
                  filterMethod=input(f'\n Ingrese la opcion deseada:')
                  while not filterMethod.isnumeric() or int(filterMethod) not in range(1,len(options)+1):
                      filterMethod=input('Invalido. Ingrese el numero de la opcion deseada:')
                  
                  if filterMethod=='1':      # Filter is Customer.
                        print(f'''\n -Buscar por cliente- \n''')
                        options=['Natural','Juridico']
                        print_options(options)
                        chose=input(f'\nIngrese la opcion deseada:')
                        while not is_int(chose) or int(chose) not in range(1,len(options)+1):
                              chose=input(f'\nInvalido. Ingrese la opcion deseada:')
                        if chose=='1':
                              id=input(f'\nIngrese la cedula del cliente:')
                              while not is_cedula(id):
                                    id=input(f'\n Invalido. Introduzca la cedula separada por puntos: Ej: "20.395.827"\n Ingrese la Cedula del cliente:')
                        else:
                              id=input(f'\nIngrese el RIF del cliente:')
                              while not is_rif(id):
                                    id=input(f'\n Invalido. Introduzca el RIF separado por guiones y con la J mayuscula. Ej: "J-29989842-2"\n Ingrese el RIF del cliente:')
                        print(f'\nPagos encontrados:')
                        aux=0
                        for shipping in self.Shipped:
                              if shipping.customer.identifierDocument==id:
                                    aux+=1
                                    print(f'{aux} {shipping.show_atr()}')
                        if aux==0:
                              print(f'\nSin resultados')
                  
                  if filterMethod=='2':      # Filter is Date
                        print(f'''\n -Buscar por fecha- \n''')
                        shipping_date_searched=set_date()
                        print(f'\n Pagos encontrados:')
                        aux=0
                        for s in self.Shipped:
                              if s.date.day==shipping_date_searched.day and s.date.month==shipping_date_searched.month and s.date.year==shipping_date_searched.year:
                                    aux+=1
                                    print(f'{aux} {s.show_atr()}')
                        if aux==0:
                              print(f'\nSin resultados')

                  if filterMethod=='3':      #Salir
                        break
            else:
                  print(f'\n No hay envios registrados')
                  break

# STATISTICS

def selection_period_to_search_and_generate_inf(self): #General para cada opcion
      print(f'\n-----Seleccion del periodo-----\n El periodo entre las fechas ingresadas debe ser un año exacto. Introduzca los datos:')
      print(f"\nIntroduzca la fecha de inicio del periodo de busqueda:")
      date_init=set_date()
      print(f"\nIntroduzca la fecha de cierre del periodo de busqueda:")
      date_final=set_date()
      while not date_init.year<date_final.year or not is_period_of_one_year(date_init,date_final):
            print(f'\n      --Periodo invalido.--')
            print(f'\nRevise los datos y recuerde que el periodo entre las fechas ingresadas debe ser un año exacto.')
            print(f"\nIntroduzca la fecha de inicio del periodo:")
            date_init=set_date()
            print(f"\nIntroduzca la fecha de cierre del periodo:")
            date_final=set_date() 
                    
      years_to_print=[]
      months_to_print=[]
      for year in range(date_init.year,date_final.year+1):
            years_to_print.append(year)
                     
      for monthNumber in range(date_init.month,13):
            months_to_print.append(monthNumber)
      
      for monthNumber in range(1,date_final.month):
            months_to_print.append(monthNumber)  
      return years_to_print,months_to_print,date_init,date_final
  

def report_sales_number_in_year(self,years_to_print,months_to_print,date_init:Date,date_final:Date): # Sales
      print('---------------Ventas por dia, mes y año---------------')
      for yearNumber in years_to_print:
            number_of_sales_year=0
            for sales in self.Sales:
                  if sales.date.year==yearNumber:
                        number_of_sales_year+=1
            print(f'\n----------Año {yearNumber}. Numero de ventas:{number_of_sales_year}.----------')
            for monthNumber in months_to_print:
                  report_sales_number_in_month(self,yearNumber,monthNumber,date_init,date_final)

def report_sales_number_in_month(self,yearNumber,monthNumber,date_init:Date,date_final:Date): # Sales
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
      number_of_sales_month=0
      for sales in self.Sales:
            if sales.date.month==monthNumber:
                  number_of_sales_month+=1
      print(f'\nMes {monthNumber}. Numero de ventas realizadas:{number_of_sales_month}.')
      print(f"\n        Diarias:(Dia:Ventas realizadas)")
      days_sales={}
      for d in range(int(date_init.day),calendary[f'{date_init.month}']+1):
            number_of_sales_day=0
            for sales in self.Sales:
                  if sales.date.day==d and sales.date.day==monthNumber and sales.date.year==yearNumber:
                        number_of_sales_day+=1
            days_sales[f'Dia:{d}']=number_of_sales_day
      print(days_sales)                                     #Cambiado para acortar las lineas de impresion en el terminal

def report_pay_number_in_year(self,years_to_print,months_to_print,date_init:Date,date_final:Date): #Payments
      print('---------------Pagos por dia, mes y año---------------')
      for yearNumber in years_to_print:
            number_of_Pay_year=0
            for Pay in self.Payments:
                  if Pay.date.year==yearNumber:
                        number_of_Pay_year+=1
            print(f'\n----------Año {yearNumber}. Numero de Pagos:{number_of_Pay_year}.----------')
            for monthNumber in months_to_print:
                  report_pay_number_in_month(self,yearNumber,monthNumber,date_init,date_final)

def report_pay_number_in_month(self,yearNumber,monthNumber,date_init:Date,date_final:Date): # Payments
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
      number_of_Pay_month=0
      for Pay in self.Payments:
            if Pay.date.month==monthNumber:
                  number_of_Pay_month+=1
      print(f'\nMes {monthNumber}. Numero de Pagos realizados:{number_of_Pay_month}.')
      print(f"\n        Diarias:(Dia:Pagos realizados)")
      days_Pay={}
      for d in range(int(date_init.day),calendary[f'{date_init.month}']+1):
            number_of_Pay_day=0
            for Pay in self.Payments:
                  if Pay.date.day==d and Pay.date.month==monthNumber and Pay.date.year==yearNumber:
                        number_of_Pay_day+=1
            days_Pay[f'Dia:{d}']=number_of_Pay_day
      print(days_Pay)                                 #Cambiado para acortar las lineas de impresion en el terminal

def report_shipping_number_in_year(self,years_to_print,months_to_print,date_init:Date,date_final:Date): # Shipped
      print('---------------Envios por dia, mes y año---------------')
      for yearNumber in years_to_print:
            number_of_Shipping_year=0
            for Shipping in self.Shipped:
                  if Shipping.date.year==yearNumber:
                        number_of_Shipping_year+=1
            print(f'\n----------Año {yearNumber}. Numero de Envios:{number_of_Shipping_year}.----------')
            for monthNumber in months_to_print:
                  report_shipping_number_in_month(self,yearNumber,monthNumber,date_init,date_final)

def report_shipping_number_in_month(self,yearNumber,monthNumber,date_init:Date,date_final:Date): # Shipped
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
      number_of_Pay_month=0
      for Shipping in self.Shipped:
            if Shipping.date.month==monthNumber:
                  number_of_Pay_month+=1
      print(f'\nMes {monthNumber}. Numero de envios realizados:{number_of_Pay_month}.')
      print(f"\n        Diarias:(Dia:Envios realizados)")
      days_Shipping={}
      for d in range(int(date_init.day),calendary[f'{date_init.month}']+1):
            number_of_Shipping_day=0
            for Shipping in self.Shipped:
                  if Shipping.date.day==d and Shipping.date.month==monthNumber and Shipping.date.year==yearNumber :
                        number_of_Shipping_day+=1
            days_Shipping[f'Dia:{d}']=number_of_Shipping_day
      print(days_Shipping)                                        #Cambiado para acortar las lineas de impresion en el terminal
