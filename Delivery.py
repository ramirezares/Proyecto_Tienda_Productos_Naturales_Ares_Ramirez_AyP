# Clase Delivery. Atr name, lastName, identifierDocument, phoneNumber
#                 Metodos: show_atr()
class Delivery:     #Delivey no es una subclase de shipping
    # TODO: Hacer docstring:
    def __init__(self,name,identifierDocument,phoneNumber):
        self.name=name
        self.identifierDocument=identifierDocument
        self.phoneNumber=phoneNumber

    def show_atr(self):
        # TODO: Hacer docstring:
        return f'''
        Nombre: {self.name}
        Cedula: {self.identifierDocument}
        Numero de telefono: {self.phoneNumber}
        '''