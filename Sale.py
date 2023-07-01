from Functions import *
from Customer import Customer
from Date import Date
class Sale:
    """_Ventas que seran registradas en la Tienda_

    Methods:
        show_atr: str

    Subclasses:
        LegalSale
    """

    def __init__(self,date:Date,saleNumber:str,saleStatus:str,customer:Customer,products:list,paymentMethod:str,shippingMethod:str):
        """_Crea una instancia de la clase Venta 'Sale'_

        Args:
            date (date): --Fecha de la venta
            saleNumber (str): --Numero de la venta
            customer (Customer): --Cliente de la venta
            products (list): --Productos que se venden
            paymentMethod (str): --Metodo de pago de la venta
            shippingMethod (str): --Metodo de envio de la venta     
            totalAmount (_type_): --Monto total de la venta
        """

        self.date=date
        self.saleNumber= saleNumber        
        self.saleStatus=saleStatus
        self.customer=customer
        self.products=products
        self.breakdownProducts=build_Products_breakdown(self.products) #Colocado para imprimir mejor los productos
        self.paymentMethod=paymentMethod
        self.shippingMethod=shippingMethod  
        self.shippingAddress=customer.address  #Se planteo agregar direccion de envio a la factura porque todo Online
        self.breakdown=build_SaletotalAmount_breakdown(paymentMethod, products)

    def show_atr(self):
        """_Muestra los atributos de una instancia de la clase Sale_

        Args:
        self -- la instancia, preteneciente a la clase Sale, de la cual se desea visualizar los atributos.

        Returns:
            str: --retorna los atributos ordenados de dicha instancia.
        """

        return f'''
        Fecha: {self.date.show_date()}              Numero de venta: {self.saleNumber}
        Cliente: {self.customer.name} C.I:{self.customer.identifierDocument}
        Estado: {self.saleStatus}
        
        Productos comprados:
        {self.breakdownProducts}
        
        Metodo de pago: {self.paymentMethod}
        Metodo de envio: {self.shippingMethod}
        Direccion: {self.shippingAddress}

        Desglose de la compra: 
        - Subtotal:{self.breakdown['Subtotal']}
        - IVA:{self.breakdown['IVA']}
        - IGTF:{self.breakdown['IGTF']}
        - Total:{self.breakdown['Total']}
        '''
    