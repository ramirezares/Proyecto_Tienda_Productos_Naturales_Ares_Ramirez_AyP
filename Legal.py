from Validations import *
from Customer import Customer

class Legal(Customer):
    #Docsting

    def __init__(self, name: str, kind:str, email: str, address: str, phoneNumber: str, identifierDocument):
        super().__init__(name, kind, email, address, phoneNumber, identifierDocument)

    def show_atr(self):
        return f'''
        Razon Social: {self.name}
        Tipo de cliente: {self.kind}
        Email: {self.email}
        Direccion: {self.address}
        Numero de telefono: {self.phoneNumber}
        RIF del cliente: {self.identifierDocument}
        '''

    def modify_atr(self, atr_number):
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
