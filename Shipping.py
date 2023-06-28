# Class Shipping. Atr: shippingService, shippingNumber, shippingCost, date
#                 Metodos: show_atr 
from Date import Date

class Shipping:
    # TODO: Hacer docstring:
    def __init__(self,date:Date,Order,shippingService:str,shippingCost:float):
        self.date=date
        self.order=Order #Nota: Cambiar el orden en el diagrama
        self.shippingService=shippingService #Nota cambiar
        self.shippingCost=shippingCost 
        if shippingService=='Delivery':
            self.Delivery=register_delivery()

    def show_atr(self):
        # TODO: Hacer docstring:
        return f'''
        Fecha: {self.date}
        Numero de envio: {self.order}
        Metodo de envio: {self.shippingService}
        Costo de envio: {self.shippingCost}
        '''