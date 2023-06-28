from Validations import *

class Customer:
    """_Clientes que son registrados e interactuan en la Tienda_

    Methods:
        show_atr: str
        modify_atr: void        
        
    Subclasses:
        Legal
        Natural
    """
    
    def __init__(self,name:str,kind:str,email:str,address:str,phoneNumber:str,identifierDocument:str):
        """_Crea una instancia de la clase Cliente_

        Args:
            name (str): --El nombre y apellido o Razon Social del cliente
            kind (str): --El tipo de cliente: natural o juridico
            email (str): --El correo del cliente
            address (str): --La direccion del cliente
            phoneNumber (str): --El numero de telefono del cliente
            identifierDocument (str): --La cedula o el rif del cliente
        """        
        
        self.name=name
        self.kind=kind
        self.email=email
        self.address=address
        self.phoneNumber=phoneNumber
        self.identifierDocument=identifierDocument

    def show_atr(self):
        """_Muestra los atributos de una instancia de la clase Cliente_

        Args:
        self -- la instancia, preteneciente a la clase cliente, de la cual se desea visualizar los atributos.

        Returns:
            str: --retorna los atributos ordenados de dicha instancia
        """
        return f'''
        Nombre: {self.name}
        Tipo de cliente: {self.kind}
        Email: {self.email}
        Direccion: {self.address}
        Numero de telefono: {self.phoneNumber}
        ID: {self.identifierDocument}
        '''
    
    def modify_atr(self,atr_number):
        """_Modifica los atributos de una instancia de la clase Cliente tomando en cuenta su tipo_

        Args:
            atr_number (int): _Representa el numero del atributo que se desea modificar, en el orden mostrado en el __init__.
        """
        if atr_number=='1':         #name
            new_name=input(f'\nIntroduzca el nuevo nombre y apellido o Razon social:')
            while not is_naturalName(new_name):
                new_name=input(f'\nInvalido. Introduzca el nuevo nombre y apellido o Razon social:')
            self.name=new_name
            print(f'\nCambios guardados.')
        if atr_number=='2':         #email
            new_email=input(f'\nIntroduzca el nuevo correo:') 
            while not is_email(new_email):
                new_email=input(f'\nInvalido. Introduzca el nuevo correo:')
            self.email=new_email
            print(f'\nCambios guardados.')
        if atr_number=='3':         #address
            new_address=input(f'''\nIntroduzca la nueva direccion(Ciudad,Urbanizacion,Casa.Estado):''')
            while not is_address(new_address):
                new_address=input(f'''\nIntroduzca la nueva direccion(Ciudad,Urbanizacion,Casa.Estado):''')
            self.address=new_address
            print(f'\nCambios guardados.')
        if atr_number=='4':         #phoneNumber
            new_phoneNumber=input(f'\nIntroduzca el nuevo numero de telefono con un solo punto (Ej: 0412.2972606):')
            while not is_phoneNumber(new_phoneNumber): 
                new_phoneNumber=input(f'\nInvalido. Introduzca el nuevo numero de telefono:')
            self.category=new_phoneNumber
            print(f'\nCambios guardados.')
        if atr_number=='5': #identifierDocument
            new_identifierDocument=input(f'\nIntroduzca la nueva identificacion:')
            while not is_cedula(new_identifierDocument):
                new_identifierDocument=input(f'\nInvalido. Introduzca la nueva identificacion:')
            self.identifierDocument=new_identifierDocument
            print(f'\nCambios guardados.')
        