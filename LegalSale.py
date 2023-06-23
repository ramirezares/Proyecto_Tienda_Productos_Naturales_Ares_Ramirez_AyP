# Modificar en el diagrama de clases
# Clase LegalSale (subclass). Atr: discount=5 deadline str
#                  Metodos: show_atr modificado

from Customer import Customer
from Sale import Sale
from Date import Date
from Functions import calculate_deadline

class LegalSale(Sale):
    """_Ventas de la clase Legal "LegalSale" que son registradas en la Tienda

    Methods:
        show_atr: str

    La clase 'LegalSale' hereda el comportamiento de la clase venta 'Sale'.
    La clase LegalSale varia en que agrega dos (2) atributos: discount y deadline.
    """

    def __init__(self,date:Date,saleNumber:str,customer:Customer,productsAmount:list,paymentMethod:str,shippingMethod:str,totalAmount,amount_of_days:int):
        """_summary_    #TODO - "Hacer docstring"

        Args:
            date (Date): _description_
            saleNumber (str): _description_
            customer (Customer): _description_
            productsAmount (list): _description_
            paymentMethod (str): _description_
            shippingMethod (str): _description_
            totalAmount (_type_): _description_
            amount_of_days (int): _description_
        """        
        super().__init__(date,saleNumber,customer,productsAmount,paymentMethod,shippingMethod,totalAmount)
        self.discount=5
        self.deadline=calculate_deadline(date,amount_of_days)
    
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