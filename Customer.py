from Functions import is_int
from Functions import is_email

# Clase Cliente. Atributos: name, email, address, phoneNumber "todos str"
#                  Metodos: show_atr() , modify_atr(atr)

class Customer:
    """_Clientes que son registrados e interactuan en la Tienda_

    Methods:
        show_atr: str
        modify_atr: void        
        
    Subclasses:
        Legal
        Natural
    """
    
    def __init__(self,name:str,email:str,address:str,phoneNumber:str):
        """_Crea una instancia de la clase Cliente_

        Args:
            name(str): --El nombre del cliente
            email (str): --El correo del cliente
            address (str): --La direccion del cliente
            phoneNumber (str): --El numero de telefono del cliente
        """        
        
        self.name=name
        self.email=email
        self.address=address
        self.phoneNumber=phoneNumber

    def show_atr(self):
        """_Muestra los atributos de una instancia de la clase Cliente_

        Args:
        self -- la instancia, preteneciente a la clase cliente, de la cual se desea visualizar los atributos.

        Returns:
            str: --retorna los atributos ordenados de dicha instancia
        """      
        return f'''
        Nombre: {self.name}
        Email: {self.email}
        Direccion: {self.address}
        Numero de telefono: {self.phoneNumber}
        '''
    
    def modify_atr(self,atr_number):
        """_Modifica los atributos de una instancia de la clase Cliente

        Args:
            atr_number (int): _Representa el numero del atributo que se desea modificar, en el orden mostrado en el __init__.
        """

        if atr_number=='1':         #name
            new_name=input('Introduzca el nuevo nombre:')
            while not new_name.isalpha() and not len(new_name)>=3 and not len(new_name)<=30:    #cortar
                new_name=input('Invalido. Introduzca el nuevo nombre:')
            self.name=new_name
            print('Cambios guardados.')

        if atr_number=='2':         #email
            new_email=input('Introduzca el nuevo correo:') 
            while not is_email(new_email):
                new_email=input('Invalido. Introduzca el nuevo correo:')
            self.email=new_email
            print('Cambios guardados.')

        if atr_number=='3':         #address
            new_address=input('''
            Introduzca la nueva direccion(Ciudad,Urbanizacion,Casa.Estado):
            ''')
            while not len(new_address)>=35 and not len(new_address)<=150:
                new_address=input('''
            Introduzca la nueva direccion(Ciudad,Urbanizacion,Casa.Estado):
            ''')
            self.address=new_address
            print('Cambios guardados.')
        
        if atr_number=='4':         #phoneNumber
            new_phoneNumber=input('Introduzca el nuevo numero de telefono:')
            prefix=False
            if new_phoneNumber[0]=="0" and new_phoneNumber[1]=="2" or new_phoneNumber[1]=="4" and new_phoneNumber[2]=="1" or new_phoneNumber[2]=="2" and new_phoneNumber[3]=="2" or new_phoneNumber[3]=="4" or new_phoneNumber[3]=="6":
                prefix= True
            while not new_phoneNumber.isnumeric() and not len(new_phoneNumber)==11 and not prefix: 
                new_phoneNumber=input('Invalido. Introduzca el nuevo numero de telefono:')
            self.category=new_phoneNumber
            print('Cambios guardados.')
         
        
