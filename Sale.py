# Clase Sale. Atr: date, costumer, productsAmount (dic 'P',A), paymentMethod, shippingMethod, totalAmount, saleNumber
#             Metodos: show_atr

from Customer import Customer

class Sale:
    # TODO: Hacer docstring:
    def __init__(self,date:str,saleNumber:str,customer:Customer,productsAmount:list,paymentMethod:str,shippingMethod:str,totalAmount):
        self.date=date
        self.saleNumber= saleNumber         #cambiar el orden en el diagrama
        self.customer=customer
        self.productsAmount=productsAmount
        self.paymentMethod=paymentMethod
        self.shippingMethod=shippingMethod  
        self.totalAmount=totalAmount

    def show_atr(self):
        # TODO: Hacer docstring:
        return f'''
        Fecha: {self.date}
        Numero de venta: {self.saleNumber}
        Cliente: {self.customer}
        Cantidad de productos: {self.productsAmount}
        Metodo de pago: {self.paymentMethod}
        Metodo de envio: {self.shippingMethod}
        Monto total: {self.saleNumber}
        '''