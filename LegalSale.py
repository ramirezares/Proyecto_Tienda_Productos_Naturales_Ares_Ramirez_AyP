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
        """_Crea una instancia de la clase 'LegalSale'_    

        Args:
            date (Date): --Fecha de la venta
            saleNumber (str): --Numero de la venta
            customer (Customer): --Cliente de la venta
            productsAmount (list): --Productos y cantidad de los mismos que se venden
            paymentMethod (str): --Metodo de pago de la venta
            shippingMethod (str): --Metodo de envio de la venta
            totalAmount (_type_): --Monto total de la venta
            amount_of_days (int): --Cantidad de dias para pago de contado. 
        """        
        super().__init__(date,saleNumber,customer,productsAmount,paymentMethod,shippingMethod,totalAmount)
        self.discount=5
        self.deadline=calculate_deadline(date,amount_of_days)
    
    def show_atr(self):
       """_Muestra los atributos de una instancia de la clase Sale_

        Args:
        self -- la instancia, preteneciente a la clase Sale, de la cual se desea visualizar los atributos.

        Returns:
            str: --retorna los atributos ordenados de dicha instancia.
        """

       return f'''
       Fecha: {self.date.show_date()}   Numero de venta: {self.saleNumber}
       Cliente: {self.customer.name}

       Cantidad de productos: {self.productsAmount} 
       
       Metodo de pago: {self.paymentMethod}
       Metodo de envio: {self.shippingMethod}
       Monto total: {self.saleNumber}
       Descuento: {self.discount}
       Fecha limite: {self.deadline.show_date()}
       '''    