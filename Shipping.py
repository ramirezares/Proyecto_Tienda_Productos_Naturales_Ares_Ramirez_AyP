# Class Shipping. Atr: shippingService, shippingNumber, shippingCost, date
#                 Metodos: show_atr 
class Shipping:
    # TODO: Hacer docstring:
    def __init__(self,shippingNumber:str,shippingService:str,shippingCost:float,date:str):
        self.date=date
        self.shippingNumber=shippingNumber #Nota: Cambiar el orden en el diagrama
        self.shippingService=shippingService #Nota cambiar
        self.shippingCost=shippingCost #

    def show_atr(self):
        # TODO: Hacer docstring:
        return f'''
        Fecha: {self.date}
        Numero de envio: {self.shippingNumber}
        Metodo de envio: {self.shippingService}
        Costo de envio: {self.shippingCost}
        '''