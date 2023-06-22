# Modificar en el diagrama de clases
# Clase LegalSale (subclass). Atr: discount=5 deadline str
#                  Metodos: show_atr modificado

from Customer import Customer
from Sale import Sale

class LegalSale(Sale):
    """_Ventas de la clase Legal "LegalSale" que son registradas en la Tienda

    Methods:
        show_atr: str
        
    Returns:
        _type_: _description_
    """    
    # TODO: Hacer docstring:
    def __init__(self,date:str,saleNumber:str,customer:Customer,productsAmount:list,paymentMethod:str,shippingMethod:str,totalAmount,discount:int,deadline:str):
        super().__init__(date,saleNumber,customer,productsAmount,paymentMethod,shippingMethod,totalAmount)
        self.discount=discount
        self.deadline=deadline
    
    def show_atr(self):
       # TODO: Hacer docstring:
       return f'''
        Fecha: {self.date}
        Numero de venta: {self.saleNumber}
        Cliente: {self.customer.name}
        Cantidad de productos: {self.productsAmount}
        Metodo de pago: {self.paymentMethod}
        Metodo de envio: {self.shippingMethod}
        Monto total: {self.saleNumber}
        Descuento: {self.discount}
        Fecha limite: {self.deadline}
        '''    