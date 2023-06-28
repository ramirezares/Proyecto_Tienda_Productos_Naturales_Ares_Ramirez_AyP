from Validations import *
from Customer import Customer

class Natural(Customer):
    #Docsting

    def __init__(self, name: str, kind: str, email: str, address: str, phoneNumber: str, identifierDocument:str):
        super().__init__(name, kind, email, address, phoneNumber, identifierDocument)

    def show_atr(self):
        return f'''
        Nombre: {self.name}
        Tipo de cliente: {self.kind}
        Email: {self.email}
        Direccion: {self.address}
        Numero de telefono: {self.phoneNumber}
        Cedula del cliente: {self.identifierDocument}
        '''
    
    def modify_atr(self, atr_number):
        if atr_number=='1':         #name
            new_name=input(f'\nIntroduzca el nombre y apellido:')
            while not is_naturalName(new_name):
                new_name=input(f'\nInvalido. Introduzca el primer nombre y primer apellido separado por un espacio:')
            self.name=new_name
            print(f'\nCambios guardados.')
        if atr_number=='2':         #email
            new_email=input(f'\nIntroduzca el nuevo correo:') 
            while not is_email(new_email):
                new_email=input(f'\nInvalido. Introduzca el nuevo correo:')
            self.email=new_email
            print(f'\nCambios guardados.')
        if atr_number=='3':         #address
            new_address=input(f'\nIntroduzca la nueva direccion(Ciudad,Urbanizacion,Casa.Estado):')
            while not is_address(new_address):
                new_address=input(f'\nIntroduzca la nueva direccion(Ciudad,Urbanizacion,Casa.Estado):')
            self.address=new_address
            print(f'\nCambios guardados.')
        if atr_number=='4':         #phoneNumber
            new_phoneNumber=input(f'\nIntroduzca el nuevo numero de telefono con un solo punto: (Ej: 0412.2972606)')
            while not is_phoneNumber(new_phoneNumber): 
                new_phoneNumber=input(f'\nInvalido. Introduzca el nuevo numero de telefono:')
            self.category=new_phoneNumber
            print(f'\nCambios guardados.')
        if atr_number=='5': #identifierDocument
            new_identifierDocument=input(f'\nIntroduzca la nueva cedula:')
            while not is_cedula(new_identifierDocument):
                new_identifierDocument=input(f'\nInvalido. Introduzca la nueva cedula:')
            self.identifierDocument=new_identifierDocument
            print(f'\nCambios guardados.')

        