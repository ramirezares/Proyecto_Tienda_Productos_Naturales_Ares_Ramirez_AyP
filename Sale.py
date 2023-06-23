from Customer import Customer
from Date import Date
class Sale:
    """_Ventas que seran registradas en la Tienda_

    Methods:
        show_atr: str

    Subclasses:
        LegalSale
    """

    def __init__(self,date:Date,saleNumber:str,customer:Customer,productsAmount:list,paymentMethod:str,shippingMethod:str,totalAmount):
        """_Crea una instancia de la clase Venta 'Sale'_

        Args:
            date (date): --Fecha de la venta
            saleNumber (str): --Numero de la venta
            customer (Customer): --Cliente de la venta
            productsAmount (list): --Productos y cantidad de los mismos que se venden
            paymentMethod (str): --Metodo de pago de la venta
            shippingMethod (str): --Metodo de envio de la venta
            totalAmount (_type_): --Monto total de la venta
        """        
        self.date=date
        self.saleNumber= saleNumber         #cambiar el orden en el diagrama
        self.customer=customer
        self.productsAmount=productsAmount
        self.paymentMethod=paymentMethod
        self.shippingMethod=shippingMethod  
        self.totalAmount=totalAmount

    def show_atr(self):
        """_Muestra los atributos de una instancia de la clase Sale_

        Args:
        self -- la instancia, preteneciente a la clase Sale, de la cual se desea visualizar los atributos.

        Returns:
            str: --retorna los atributos ordenados de dicha instancia.
        """

        return f'''
        Fecha: {self.date.show_date()}
        Numero de venta: {self.saleNumber}
        Cliente: {self.customer}
        Cantidad de productos: {self.productsAmount}
        Metodo de pago: {self.paymentMethod}
        Metodo de envio: {self.shippingMethod}
        Monto total: {self.saleNumber}
        '''