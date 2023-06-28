from Date import Date
from Product import Product
from Natural import Natural
from Legal import Legal
from Pay import Pay

from Validations import *

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

def set_date():
      year=input('Ingrese el año actual:')
      while not is_int(year) or not len(year)==4:
            year=input('Año invalido. Ingrese el año actual:')
      
      month=input('Ingrese el numero del mes actual:')
      while not is_int(month) or not len(month)>=1 or not len(month)<=2:
            month=input('Mes invalido. Ingrese el numero del mes actual:')
      
      day=input('Ingrese el numero del dia actual:')
      while not is_int(day) or not len(day)>=1 or not len(day)<=2:
            day=input('Dia invalido. Ingrese el numero del dia actual:')
      date=Date(int(day),int(month),int(year))
      
      while not is_date(Date(int(day),int(month),int(year))):
            print(f'\n Datos invalidos. Por favor revise e ingrese nuevamente.\n')      
            year=input('Ingrese el año actual:')
            while not is_int(year) or not len(year)==4:
                  year=input('Año invalido. Ingrese el año actual:')
            
            month=input('Ingrese el numero del mes actual:')
            while not is_int(month) or not len(month)>=1 or not len(month)<=2:
                  month=input('Mes invalido. Ingrese el numero del mes actual:')
            
            day=input('Ingrese el numero del dia actual:')
            while not is_int(day) or not len(day)>=1 or not len(day)<=2:
                  day=input('Ingrese el numero del dia actual:')
            date=Date(int(day),int(month),int(year))
      
      print('\n Fecha ingresada correctamente. \n')
      return date

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
          print(f'\n')
          print_options(matchedAlternatives)
          chose=input(f'\nSeleccione la opcion deseada:')
          while not chose.isnumeric() or int(chose) not in range(1,len(matchedAlternatives)+1):
              chose=input(f'\n Opcion invalida. Ingrese la opcion deseada:')
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
          print(f'\nOpciones encontradas con el filtro:')
          print(f'\n')
          print_options(matchedAlternatives)
          chose=input(f'\nSeleccione la opcion deseada:')
          while not chose.isnumeric() or int(chose) not in range(1,len(matchedAlternatives)+1):
              chose=input(f'\nOpcion invalida. Ingrese la opcion deseada:')
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
          print(f'\nOpciones encontradas con el filtro:')
          print(f'\n')
          print_options(matchedAlternatives)
          chose=input(f'\nSeleccione la opcion deseada:')
          while not chose.isnumeric() or int(chose) not in range(1,len(matchedAlternatives)+1):
              chose=input(f'\n Opcion invalida. Ingrese la opcion deseada:')
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
               print(f'\n')
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

def vef_not_is_id_in_registered_customers(self,id):         #Revisar por que no corre
      if len(self.Customers)>0:
            for C in self.Customers:
                  if C.identifierDocument==id:
                        return True
      return False

def add_customer(self):
        while True:
            print(f'''\n-----Agregar cliente-----\n \nIngrese el tipo de cliente:\n''')
            options=['Natural','Juridico','Salir']
            print_options(options)
            chose=input('Ingrese la opcion deseada:')
            while not chose.isnumeric() or int(chose) not in range(1,len(options)+1):
                  chose=('Invalido. Ingrese la opcion deseada:')
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
                while not is_cedula(identifierDocument) or vef_not_is_id_in_registered_customers(self,id):
                    identifierDocument=input(f'Invalida o ya registrada. Ej: 20.982.756 \n Introduzca la cedula del cliente:')
                new_customer=Natural(name,kind,email,address,phoneNumber,identifierDocument)
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
                while not is_rif(rif) or vef_not_is_id_in_registered_customers(self,rif):
                    rif=input(f'\n Invalido o ya registrado. Ej: "J-29989842-2" \n Introduzca el RIF del cliente:')
                new_customer=Legal(socialReason,kind,email,address,phoneNumber,rif)
                return new_customer
        
def search_customer(self):
        while True:
               if len(self.Customers)>0:
                  print(f'''\n -----Buscar cliente----- \n''')
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
                     print('No hay clientes registrados.')

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
                  print('No hay clientes registrados.')

def del_customer(self):
        if len(self.Customers)==0:
              print('No hay clientes registrados.')
        if len(self.Customers)>0:          
            print(f'''\n-----Eliminar cliente-----\n Seleccione el cliente a eliminar:\n''')
            for idx in range(len(self.Customers)):
                print(f'{idx+1} {self.Customers[idx].show_atr()}')
            chose=input('Introduzca el numero del cliente a eliminar:')
            while not chose.isnumeric() or int(chose) not in range(1,len(self.Customers)+1):
                  chose=input('Invalido. Introduzca el numero del cliente a eliminar:')
            idx_product_to_del=int(chose)-1
            self.Customers.pop(idx_product_to_del)
            print('Eliminado.')

def generate_bill(self,sale,val):
      print(f'\n -Generar factura-\n')
      if len(self.Sales)>0:
            if val==False:
                  aux=0
                  for sale in self.Sales:
                        print(f'{aux+1} {sale.saleNumber} {sale.customer} {sale.customer.identifierDocument} {sale.breakdown}')
                        aux+=1
                  chose=input(f'\nIngrese la venta deseada:')
                  while not is_int(chose) or int(chose) not in range(1,len(self.Sales)+1):
                        chose=input(f'\n Invalido. Ingrese el numero la venta deseada:')
                  sale=self.Sales[int(chose)-1]
                  print(sale.show_atr())        # Falta un comando para que mande a imprimirlo en una impresora JAJAJAJ
            if val==True:
                  print(sale.show_atr())
      else:
            print('No hay ventas registradas')
      

def calculate_saleNumber(self):
      if len(self.Sales)==0:
            saleNumber=1
      else:
            registered_sales=len(self.Sales)
            saleNumber=registered_sales+1
      saleNumber_inStr=str(saleNumber)
      return saleNumber_inStr

def select_naturalCustomer(self):
      while True:
            print(f'\n-----Seleccion de cliente-----\n')
            options=['Buscar cliente.','Registrar cliente.','Salir']
            print_options(options)
            chose=input(f'\nIngrese la opcion deseada:')
            while not is_int(chose) or int(chose) not in range(1,len(options)+1):
                  chose=input('Invalido. Ingrese la opcion deseada:')
            if chose=='1':
                  id=input(f'\nIntroduzca la cedula del cliente: ')
                  while not is_cedula(id):
                        id=input(f'\n Invalido. Introduzca la cedula separada por puntos: Ej: "20.395.827"\n Ingrese la Cedula del cliente:')
                  sum=0
                  for c in self.Customers:
                        if c.identifierDocument==id:
                              sum=+1 
                  if sum==0:
                        print(f'\nCliente no encontrado.')
                        continue
                  for c in self.Customers:
                        if c.identifierDocument==id:
                              selected_customer=c
                  print(f"\nCliente seleccionado: {selected_customer.show_atr()}")
                  return selected_customer
            if chose=='2':
                  new_customer=add_customer(self)
                  self.Customers.append(new_customer)
                  print(f'\n Registrado. \n')
            if chose=='3':
                  break

def select_legalCustomer(self):
      while True:
            print(f'\n-----Seleccion de cliente-----')
            options=['Buscar cliente.','Registrar cliente.','Salir']
            print_options(options)
            chose=input('Ingrese la opcion deseada:')
            while not is_int(chose) or int(chose) not in range(1,len(options)+1):
                  chose=input('Invalido. Ingrese la opcion deseada:')
            if chose=='1':
                  id=input('Introduzca el RIF del cliente: ')
                  while not is_rif(id):
                        id=input(f'\n Invalido. Introduzca el RIF separado por guiones y con la J mayuscula: Ej: "J-29989842-2"\n Ingrese el RIF del cliente:')
                  sum=0
                  for c in self.Customers:
                        if c.identifierDocument==id:
                              sum=+1 
                  if sum==0:
                        print(f'\nCliente no encontrado.')
                        continue
                  for c in self.Customers:
                        if c.identifierDocument==id:
                              selected_customer=c
                  print(f"\nCliente seleccionado: {selected_customer.show_atr()}")
                  return selected_customer
            if chose=='2':
                  new_customer=add_customer(self)
                  self.Customers.append(new_customer)
                  print(f'\n Registrado. \n')
            if chose=='3':
                  break
   
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
      chose=input('Ingrese el numero de la opcion deseada:')
      while not is_int(chose) or int(chose)-1 not in range(len(options)):
            chose=input('Invalido. Ingrese el numero de la opcion deseada:')
      keyValues={}
      for n in range(1,len(options)+1):
            keyValues[f'{n}']=options[n-1]
      return keyValues[chose]
            
def select_shippingMethod():
      print(f'\n-----Seleccion del metodo de envio-----\n')
      options=['Envio de paquetes','Delivery']
      print_options(options)
      chose=input('Ingrese el numero de la opcion deseada:')
      while not is_int(chose) or int(chose)-1 not in range(len(options)):
            chose=input('Invalido. Ingrese el numero de la opcion deseada:')
      keyValues={}
      for n in range(1,len(options)+1):
            keyValues[f'{n}']=options[n-1]
      return keyValues[chose]
          
def calculate_subtotal(products):
      subtotal=0
      for dic in products:
            value=int(dic["subtotal"])
            subtotal+=value
      return subtotal

def calculate_SaletotalAmount(subtotal,IVA,IGFT):
      Total=0
      IVA_for_sale=subtotal*int(IVA[0:1])
      IGTF_for_sale=subtotal*int(IGFT[0])
      Total=subtotal-IVA_for_sale-IGTF_for_sale
      return Total

def calculate_LegalSaletotalAmount(subtotal,Discount,IVA,IGFT):
      Total=0
      Discount_for_sale=subtotal*int(Discount[0])
      subtotal-=Discount_for_sale
      IVA_for_sale=subtotal*int(IVA[0:1])
      IGTF_for_sale=subtotal*int(IGFT[0])
      Total=subtotal+IVA_for_sale+IGTF_for_sale
      return Total

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

def build_SaletotalAmount_breakdown(products):                       #Revisar 
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
      return Breakdown

def build_LegalSaletotalAmount_breakdown(products):
      items_for_breakdown=['Subtotal','Discount','IVA','IGTF','Total'] #Ver que pide LegalSale
      Breakdown={}
      subtotal=calculate_subtotal(products)
      Discount="5%"
      IVA="16%"
      IGTF="3%"
      Total=calculate_LegalSaletotalAmount(subtotal,Discount,IVA,IGTF)
      values=[subtotal,IVA,IGTF,Total]
      i=0
      for item in items_for_breakdown:
            Breakdown[f'{item}']=values[i]
            i+=1
      return Breakdown

def search_sale(self): #Cliente Date Monto total
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
                        chose=input('Ingrese la opcion deseada:')
                        while not is_int(chose) or int(chose) not in range(1,len(options)+1):
                              chose=input('Invalido. Ingrese la opcion deseada:')
                        if chose=='1':
                              id=input('Ingrese la cedula del cliente:')
                              while not is_cedula(id):
                                    id=input(f'\n Invalido. Introduzca la cedula separada por puntos: Ej: "20.395.827"\n Ingrese la Cedula del cliente:')
                        if chose=='2':
                              id=input('Ingrese el RIF del cliente:')
                              while not is_rif(id):
                                    id=input(f'\n Invalido. Introduzca el RIF separado por guiones y con la J mayuscula. Ej: "J-29989842-2"\n Ingrese el RIF del cliente:')
                        print('Ventas encontradas:')
                        aux=0
                        for s in self.Sales:
                              if s.customer.identifierDocument==id:
                                    aux+=1
                                    print(f'{aux} {self.Sales[s].show_atr()}')
                        if aux==0:
                              print('Sin resultados')
                  
                  if filterMethod=='2':      # Filter is Date
                        print(f'''\n -Buscar por fecha- \n''')
                        date=set_date()
                        print('Ventas encontradas:')
                        aux=0
                        for s in self.Sales:
                              if s.date==date:
                                    aux+=1
                                    print(f'{aux} {self.Sales[s].show_atr()}')
                        if aux==0:
                              print('Sin resultados')

                  if filterMethod=='3':      # Filter is TotalAmount
                        print(f'''\n -Buscar por monto total- \n''')
                        matchedAlternatives=[]
                        for s in self.Sales:
                          if s.breakdown['Total'] not in matchedAlternatives:
                                matchedAlternatives.append(s)
                        print('Ventas encontradas:')
                        for i in range(len(matchedAlternatives)):
                              print(f'{i+1}. {matchedAlternatives[i]}')
                        
                  if filterMethod=='4':      # Salir
                        break
            else:
                  print('No hay ventas registradas')
                  break

def get_paymentCurrency(sale):
      if sale.paymentMethod=='Transferencia (Bs)' or sale.paymentMethod=='Pago Movil (Bs)':
            return 'Bolivares Bs.'

      elif sale.paymentMethod=='Zelle ($)' or sale.paymentMethod=='Cash ($)':
            return 'Dolares USD'
      else:
            return ''

def search_pay(self):
      if len(self.sale)>0:
            pass
      else:
            print('No hay ventas registradas. No hay pagos registrados porque no se han realizado ventas.')

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
                          {'Nombre':'Yuumy',
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
                  chose=input(f'\nIngrese el numero de la opcion deseada:')
            shippingCompany=options[int(chose)-1]
            print(f'\n')
            distanceOptions=['Envio de corta distancia','Envio de larga distancia']
            print_options(distanceOptions)
            distance=input(f'\nIngrese el numero de la opcion:')
            while not is_int(distance) or int(distance) not in range(1,len(distanceOptions)+1):
                  chose=input(f'\nIngrese el numero de la opcion deseada:')
            shippingDistance=distanceOptions[int(chose)-1]
            shippingCost=0
            for dic in ShippingServices:
                  if dic['Nombre']==shippingCompany:
                        shippingCost=dic[f'{shippingDistance}']
            return shippingCost

      elif sale.shippingMethod=='Delivery':
            pass

      else:
            return 0.0
      
      