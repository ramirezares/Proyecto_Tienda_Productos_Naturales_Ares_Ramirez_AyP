# Clase Cliente legal (subclase). Atributos extras: social reason, rif
#                  Metodos que modificar: show_atr() , modify_atr(atr)

from Costumer import Costumer

class Legal(Costumer):
    def __init__(self,name:str,email:str,address:str,phoneNumber:str,socialReason:str,rif:str):
        super().__init__(name,email,address,phoneNumber)
        self.socialReason=socialReason
        self.rif=rif

    def show_atr(self):
       return f'''
       Nombre: {self.name}
       Email: {self.email}
       Direccion: {self.address}
       Numero de telefono: {self.phoneNumber}
       Razon social: {self.socialReason}
       RIF: {self.rif}
       '''
    