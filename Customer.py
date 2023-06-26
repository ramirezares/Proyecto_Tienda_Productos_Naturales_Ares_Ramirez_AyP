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
    
    def __init__(self,name:str,kind:str,email:str,address:str,phoneNumber:str,identifierDocument):
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

        if self.kind=='Natural':
            return f'''
            Nombre: {self.name}
            Tipo de cliente: {self.kind}
            Email: {self.email}
            Direccion: {self.address}
            Numero de telefono: {self.phoneNumber}
            Cedula del cliente: {self.identifierDocument}
            '''
        
        if self.kind=='Juridico':
            return f'''
            Razon Social: {self.name}
            Tipo de cliente: {self.kind}
            Email: {self.email}
            Direccion: {self.address}
            Numero de telefono: {self.phoneNumber}
            RIF del cliente: {self.identifierDocument}
            '''
    
    def modify_atr(self,atr_number):
        """_Modifica los atributos de una instancia de la clase Cliente tomando en cuenta su tipo_

        Args:
            atr_number (int): _Representa el numero del atributo que se desea modificar, en el orden mostrado en el __init__.
        """
        if self.kind=='Natural':
            if atr_number=='1':         #name
                new_name=input('Introduzca el nombre y apellido:')
                while not is_naturalName(new_name):
                    new_name=input('Invalido. Introduzca el primer nombre y primer apellido separado por un espacio:')
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
                Introduzca la nueva direccion(Ciudad,Urbanizacion,Casa.Estado):''')
                while not is_address(new_address):
                    new_address=input('''
                Introduzca la nueva direccion(Ciudad,Urbanizacion,Casa.Estado):''')
                self.address=new_address
                print('Cambios guardados.')

            if atr_number=='4':         #phoneNumber
                new_phoneNumber=input('Introduzca el nuevo numero de telefono con un solo punto: (Ej: 0412.2972606)')
                while not is_phoneNumber(new_phoneNumber): 
                    new_phoneNumber=input('Invalido. Introduzca el nuevo numero de telefono:')
                self.category=new_phoneNumber
                print('Cambios guardados.')

            if atr_number=='5': #identifierDocument
                new_identifierDocument=input('Introduzca la nueva cedula:')
                while not is_cedula(new_identifierDocument):
                    new_identifierDocument=input('Invalido. Introduzca la nueva cedula:')
                self.identifierDocument=new_identifierDocument
                print('Cambios guardados.')

        if self.kind=='Juridico':
            if atr_number=='1':         #socialReason
                new_socialReazon=input('Introduzca la Razon Social:')
                while not is_socialReason(new_socialReazon):
                    new_socialReazon=input('Invalido. Introduzca el nuevo nombre:')
                self.name=new_socialReazon
                print('Cambios guardados.')

            if atr_number=='2':         #email
                new_email=input('Introduzca el nuevo correo:') 
                while not is_email(new_email):
                    new_email=input('Invalido. Introduzca el nuevo correo:')
                self.email=new_email
                print('Cambios guardados.')

            if atr_number=='3':         #address
                new_address=input('''
                Introduzca la nueva direccion(Ciudad,Urbanizacion,Casa.Estado):''')
                while not is_address(new_address):
                    new_address=input('''
                Introduzca la nueva direccion(Ciudad,Urbanizacion,Casa.Estado):''')
                self.address=new_address
                print('Cambios guardados.')

            if atr_number=='4':         #phoneNumber
                new_phoneNumber=input('Introduzca el nuevo numero de telefono con un solo punto: (Ej: 0412.2972606)')
                while not is_phoneNumber(new_phoneNumber): 
                    new_phoneNumber=input('Invalido. Introduzca el nuevo numero de telefono:')
                self.category=new_phoneNumber
                print('Cambios guardados.')

            if atr_number=='5':         #RIF
                new_rif=input('''Introduzca el nuevo RIF:''')
                while not is_rif(new_rif):
                    new_rif=input('''Invalido. Introduzca el nuevo RIF:''')
                self.rif=new_rif
                print('Cambios guardados.')

