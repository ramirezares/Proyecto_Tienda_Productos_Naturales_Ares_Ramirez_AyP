# Clase Delivery. Atr name, lastName, identifierDocument, phoneNumber
#                 Metodos: show_atr()

class Delivery:     #Delivey no es una subclase de shipping
    # TODO: Hacer docstring:
    def __init__(self,name,lastName,identifierDocument,phoneNumber):
        self.name=name
        self.lastName=lastName
        self.identifierDocument=identifierDocument
        self.phoneNumber=phoneNumber

    def show_atr(self):
        # TODO: Hacer docstring:
        return f'''
        Nombre: {self.name}
        Apellido: {self.lastName}
        Cedula: {self.identifierDocument}
        Numero de telefono: {self.phoneNumber}
        '''