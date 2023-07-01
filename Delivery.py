class Delivery:     
    """_Personas (Delivery's) que llevaran los envios (Shipping) en el caso que se indique_
    
    Methods:
        show_atr: str
    
    """    

    def __init__(self,name:str,identifierDocument:str,phoneNumber:str):
        self.name=name
        self.identifierDocument=identifierDocument
        self.phoneNumber=phoneNumber

    def show_atr(self):
        """_Muestra los atributos de una instancia de la clase Delivery_

        Returns:
            str: --retorna los atributos ordenados de dicha instancia"""
        
        return f'''
        Nombre: {self.name}
        Cedula: {self.identifierDocument}
        Numero de telefono: {self.phoneNumber}
        '''