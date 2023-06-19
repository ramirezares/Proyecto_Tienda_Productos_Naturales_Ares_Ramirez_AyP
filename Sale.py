# Clase Sale. Atr: date, costumer, productsAmount (dic 'P',A), paymentMethod, shippingMethod, totalAmount, saleNumber
#             Metodos: show_atr

from Costumer import Costumer

class Sale:
    def __init__(self,date:str,saleNumber:str,costumer:Costumer,productsAmount:list,paymentMethod:str,shippingMethod:str,totalAmount):
        self.date=date
        self.saleNumber= saleNumber         #cambiar el orden en el diagrama
        self.costumer=costumer
        self.productsAmount=productsAmount
        self.paymentMethod=paymentMethod
        self.shippingMethod=shippingMethod  
        self.totalAmount=totalAmount

    def show_atr(self):
        return f'''
        Fecha: {self.date}
        Numero de venta: {self.saleNumber}
        Cliente: {self.costumer}
        Cantidad de productos: {self.productsAmount}
        Metodo de pago: {self.paymentMethod}
        Metodo de envio: {self.shippingMethod}
        Monto total: {self.saleNumber}
        '''