# Clase Cliente. Atributos: name, email, address, phoneNumber "todos str"
#                  Metodos: show_atr() , modify_atr(atr)

class Costumer:
    def __init__(self,name:str,email:str,address:str,phoneNumber:str):
        self.name=name
        self.email=email
        self.address=address
        self.phoneNumber=phoneNumber

    def show_atr(self):
        return f'''
        Nombre: {self.name}
        Email: {self.email}
        Direccion: {self.address}
        Numero de telefono: {self.phoneNumber}
        '''