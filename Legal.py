from Validations import *
from Customer import Customer

class Legal(Customer):
    """_Clientes del tipo Natural que son registrados e interactuan en la Tienda_

    Methods:
        show_atr: str
        modify_atr: void 
    """    

    def __init__(self, name: str, kind:str, email: str, address: str, phoneNumber: str, identifierDocument):
        super().__init__(name, kind, email, address, phoneNumber, identifierDocument)
        """_La clase llama al constructor de su superclase_
        """        

    def show_atr(self):
        """_Muestra los atributos de una instancia de la clase Natural
        
        Returns:
            str: --retorna los atributos ordenados de dicha instancia
        """

        return f'''
        Razon Social: {self.name}
        Tipo de cliente: {self.kind}
        Email: {self.email}
        Direccion: {self.address}
        Numero de telefono: {self.phoneNumber}
        RIF del cliente: {self.identifierDocument}
        '''

    def modify_atr(self, atr_number):
        """_Modifica los atributos de una instancia de la clase_

        Returns:
            void
        """        
        
        if atr_number=='1':         #socialReason
            new_socialReazon=input(f'\nIntroduzca la Razon Social:')
            while not is_socialReason(new_socialReazon):
                new_socialReazon=input(f'\nInvalido. Introduzca el nuevo nombre:')
            self.name=new_socialReazon
            print(f'\nCambios guardados.')
        if atr_number=='2':         #email
            new_email=input(f'\nIntroduzca el nuevo correo:') 
            while not is_email(new_email):
                new_email=input(f'\nInvalido. Introduzca el nuevo correo:')
            self.email=new_email
            print(f'\nCambios guardados.')
        if atr_number=='3':         #address
            new_address=input(f'\n Introduzca la nueva direccion(Ciudad,Urbanizacion,Casa.Estado):')
            while not is_address(new_address):
                new_address=input(f'\n Introduzca la nueva direccion(Ciudad,Urbanizacion,Casa.Estado):')
            self.address=new_address
            print(f'\nCambios guardados.')
        if atr_number=='4':         #phoneNumber
            new_phoneNumber=input(f'\nIntroduzca el nuevo numero de telefono con un solo punto (Ej: 0412.2972606):')
            while not is_phoneNumber(new_phoneNumber): 
                new_phoneNumber=input(f'\nInvalido. Introduzca el nuevo numero de telefono:')
            self.category=new_phoneNumber
            print(f'\nCambios guardados.')
        if atr_number=='5':         #RIF
            new_rif=input(f'\nIntroduzca el nuevo RIF:')
            while not is_rif(new_rif):
                new_rif=input(f'\nInvalido. Introduzca el nuevo RIF:')
            self.rif=new_rif
            print(f'\nCambios guardados.')
