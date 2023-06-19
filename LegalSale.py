# Modificar en el diagrama de clases
# Clase LegalSale (subclass). Atr: discount=5 deadline str
#                  Metodos: show_atr modificado

from Costumer import Costumer
from Sale import Sale

class LegalSale(Sale):
    def __init__(self,date:str,saleNumber:str,costumer:Costumer,productsAmount:list,paymentMethod:str,shippingMethod:str,totalAmount,discount:int,deadline:str):
        super().__init__(date,saleNumber,costumer,productsAmount,paymentMethod,shippingMethod,totalAmount)
        self.discount=discount
        self.deadline=deadline
    
    def show_atr(self):
       return f'''
        Fecha: {self.date}
        Numero de venta: {self.saleNumber}
        Cliente: {self.costumer}
        Cantidad de productos: {self.productsAmount}
        Metodo de pago: {self.paymentMethod}
        Metodo de envio: {self.shippingMethod}
        Monto total: {self.saleNumber}
        Descuento: {self.discount}
        Fecha limite: {self.deadline}
        '''    