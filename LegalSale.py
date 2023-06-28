from Functions import *
from Customer import Customer
from Sale import Sale
from Date import Date

class LegalSale(Sale):
    """_Ventas de la clase Legal "LegalSale" que son registradas en la Tienda
                    #TODO: 'cambiar el orden en el diagrama'
    Methods:
        show_atr: str

    La clase 'LegalSale' hereda el comportamiento de la clase venta 'Sale'.
    La clase LegalSale varia en que agrega dos (2) atributos: discount y deadline.
    """

    def __init__(self,date:Date,saleNumber:str,customer:Customer,products:list,paymentMethod:str,shippingMethod:str,amount_of_days:int):
        """_Crea una instancia de la clase 'LegalSale'_    

        Args:
            date (Date): --Fecha de la venta
            saleNumber (str): --Numero de la venta
            customer (Customer): --Cliente de la venta
            productsAmountPriceSubtotal (list): --Productos y cantidad de los mismos que se venden #TODO: Arreglar
            paymentMethod (str): --Metodo de pago de la venta
            shippingMethod (str): --Metodo de envio de la venta
            totalAmount (_type_): --Monto total de la venta
            amount_of_days (int): --Cantidad de dias para pago de contado. 
        """        
        super().__init__(date,saleNumber,customer,products,paymentMethod,shippingMethod)
        self.shippingAddress=customer.address  #Se planteo agregar direccion de envio a la factura porque todo Online
        self.breakdownProducts=build_Products_breakdown(self.products) #Colocado para imprimir mejor los productos
        self.discount=5
        self.deadline=calculate_deadline(date,amount_of_days)
        self.breakdown=build_LegalSaletotalAmount_breakdown(products)   #Modificar, ver Sale
    
    def show_atr(self):
       """_Muestra los atributos de una instancia de la clase Sale_

        Args:
        self -- la instancia, preteneciente a la clase Sale, de la cual se desea visualizar los atributos.

        Returns:
            str: --retorna los atributos ordenados de dicha instancia.
        """

       return f'''
       Fecha: {self.date.show_date()}   Numero de venta: {self.saleNumber}
       Cliente: {self.customer.show_atr()}

       Productos comprados:
       {self.breakdownProducts}
    
       Metodo de pago: {self.paymentMethod}
       Metodo de envio: {self.shippingMethod}
       Direccion: {self.shippingAddress}
       Fecha limite de pago: {self.deadline.show_date()}
       
        Desglose de la compra: 
        - Subtotal:{self.breakdown['Subtotal']}
        - Descuento: {self.breakdown['Discount']}
        - IVA:{self.breakdown['IVA']}
        - IGTF:{self.breakdown['IGTF']}
        - Total:{self.breakdown['Total']}
       '''    