from Validations import is_email
from Validations import is_phoneNumber
from Validations import is_rif
from Validations import is_address

from Customer import Customer

class Legal(Customer):
    """_Clientes de la clase Legal que son registrados e interactuan en la Tienda_

    Methods:
        show_atr: str
        modify_atr: void

    La clase Legal hereda el comportamiento de la clase Cliente 'Customer'.
    La clase Legal varia en que tiene dos (2) atributos adicionales distintos de la clase anterior: razonSocial y rif.
    El atributo 'razonSocial" toma la pocicion de 'name' en el constructor de la superclase.
    """

    def __init__(self,socialReason:str,email:str,address:str,phoneNumber:str,rif:str):
        """_Crea una instancia de la clase Legal_

        Args:
            socialReason (str): --La razon social (nombre del registo) del cliente Legal (empresa).
            email (str): --El correo del cliente Legal.
            address (str): --La direccion del cliente Legal.
            phoneNumber (str): --El numero de telefono del cliente Legal.
            rif (str): --RIF de la empresa
        
        La superclase 'Customer' extiende su constructor y la subclase Legal adiciona al metodo constructor para conformar el suyo.     
        """        
        super().__init__(socialReason,email,address,phoneNumber)
        self.rif=rif

    def show_atr(self):
       """_Muestra los atributos de una instancia de la clase Legal_

        Args:
        self -- la instancia, preteneciente a la clase Legal, de la cual se desea visualizar los atributos.

        Returns:
            str: --retorna los atributos ordenados de dicha instancia.

        La subclase 'Legal' anula el metodo del mismo nombre de la superclase 'Customer'.
        Lo hace para remplazar el metodo pero mantiene el mismo comportamiento, solo que integrando los nuevos atributos.
        """
       return f'''
       Razon social: {self.name}
       Email: {self.email}
       Direccion: {self.address}
       Numero de telefono: {self.phoneNumber}
       RIF: {self.rif}
       '''
    
    def modify_atr(self,atr_number):
        """_Modifica los atributos de una instancia de la clase Legal_

        Args:
            atr_number (int): _Representa el numero del atributo que se desea modificar, en el orden mostrado en el __init__.
        
        La subclase 'Legal' anula el metodo del mismo nombre de la superclase 'Customer'.
        Lo hace para remplazar el metodo pero mantiene el mismo comportamiento, solo que integrando los nuevos atributos.
        """

        if atr_number=='1':         #socialReason
            new_socialReazon=input('Introduzca la Razon Social:')
            while not new_socialReazon.isalnum() and not len(new_socialReazon)>=10 and not len(new_socialReazon)<=50:    
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
            while is_address(new_address):
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

