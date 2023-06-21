# Clase Cliente legal (subclase). Atributos extras: social reason, rif
#                  Metodos que modificar: show_atr() , modify_atr(atr)

from Customer import Customer

class Legal(Customer):
    # TODO: Hacer docstring:
    def __init__(self,name:str,email:str,address:str,phoneNumber:str,socialReason:str,rif:str):
        super().__init__(name,email,address,phoneNumber)
        self.socialReason=socialReason
        self.rif=rif

    def show_atr(self):
       # TODO: Hacer docstring:
       return f'''
       Nombre: {self.name}
       Email: {self.email}
       Direccion: {self.address}
       Numero de telefono: {self.phoneNumber}
       Razon social: {self.socialReason}
       RIF: {self.rif}
       '''
    