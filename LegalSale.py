from Functions import *
from Customer import Customer
from Sale import Sale
from Date import Date

class LegalSale(Sale):
    """_Ventas de la clase Legal "LegalSale" que son registradas en la Tienda.
    Methods:
        show_atr: str.

    La clase 'LegalSale' hereda el comportamiento de la clase venta 'Sale'.
    La clase LegalSale varia en que agrega dos (2) atributos: discount y deadline.
    """

    def __init__(self,date:Date,saleNumber:str,saleTime:str,saleStatus:str,customer:Customer,products:list,paymentMethod:str,shippingMethod:str,amount_of_days:int):
        """_Crea una instancia de la clase 'LegalSale'_    

        Args:
            date (Date): --Fecha de la venta.
            saleNumber (str): --Numero de la venta.
            customer (Customer): --Cliente de la venta.
            productsAmountPriceSubtotal (list): --Productos y cantidad de los mismos que se venden.
            paymentMethod (str): --Metodo de pago de la venta.
            shippingMethod (str): --Metodo de envio de la venta.
            totalAmount (_type_): --Monto total de la venta.
            amount_of_days (int): --Cantidad de dias para pago de contado .
        """        
        super().__init__(date,saleNumber,saleStatus,customer,products,paymentMethod,shippingMethod)
        self.saleTime=saleTime
        self.shippingAddress=customer.address  #Se planteo agregar direccion de envio a la factura porque todo es Online
        self.breakdownProducts=build_Products_breakdown(self.products) #Colocado para imprimir mejor los productos
        discount=calculate_discount(saleTime)
        self.discount=discount
        self.deadline=calculate_deadline(saleTime,date,amount_of_days)
        self.breakdown=build_LegalSaletotalAmount_breakdown(paymentMethod,discount,products)   
        
    def show_atr(self):
        """_Muestra los atributos de una instancia de la clase Sale_

        Args:
        self -- la instancia, preteneciente a la clase Sale, de la cual se desea visualizar los atributos.

        Returns:
            str: --retorna los atributos ordenados de dicha instancia.
        """

        if self.saleTime=="Pago a credito" and type(self.deadline)==Date: 
           return f'''
    Fecha: {self.date.show_date()}   Numero de venta: {self.saleNumber}
    Cliente: {self.customer.name} RIF:{self.customer.identifierDocument}
    Estado: {self.saleStatus}

    Productos comprados:
    {self.breakdownProducts}

    Metodo de pago: {self.paymentMethod}
    Metodo de envio: {self.shippingMethod}
    Direccion: {self.shippingAddress}
    Fecha limite de pago: {self.deadline.show_date()}

     Desglose de la compra: 
     - Subtotal:{self.breakdown['Subtotal']}
     - IVA:{self.breakdown['IVA']}
     - IGTF:{self.breakdown['IGTF']}
     - Total:{self.breakdown['Total']}
    '''
        else:
            return f'''
    Fecha: {self.date.show_date()}   Numero de venta: {self.saleNumber}
    Cliente: {self.customer.name} RIF:{self.customer.identifierDocument}
    Estado: {self.saleStatus}

    Productos comprados:
    {self.breakdownProducts}

    Metodo de pago: {self.paymentMethod}
    Metodo de envio: {self.shippingMethod}
    Direccion: {self.shippingAddress}

     Desglose de la compra: 
     - Subtotal:{self.breakdown['Subtotal']}
     - Descuento:{self.breakdown['Discount']}
     - IVA:{self.breakdown['IVA']}
     - IGTF:{self.breakdown['IGTF']}
     - Total:{self.breakdown['Total']}
    '''
