# Clase Cliente natural (subclase). Atributos extras: lastname, identifierDocument "Cedula"
#                  Metodos que modificar: show_atr() , modify_atr(atr)

from Customer import Customer

class Natural(Customer):
    # TODO: Hacer docstring:
    def __init__(self,name:str,email:str,address:str,phoneNumber:str,lastName:str,identifierDocument:str):
        super().__init__(name,email,address,phoneNumber)
        self.lastName=lastName
        self.identifierDocument=identifierDocument

    def show_atr(self):
       # TODO: Hacer docstring:
       return f'''
       Nombre: {self.name}
       Apellido: {self.lastName}
       Email: {self.email}
       Direccion: {self.address}
       Numero de telefono: {self.phoneNumber}
       Cedula: {self.identifierDocument}
       '''