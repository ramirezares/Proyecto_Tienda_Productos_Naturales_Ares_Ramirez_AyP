from Date import Date
from Customer import Customer
from Functions import register_delivery

class Shipping:
    """_Envios que realizara la tienda _
    """    

    def __init__(self,date:Date,customer:Customer,shippingNumber,Order,shippingService:str,shippingCost:float):
        """_Crea una instancia de la clase Shipping_

        Args:
            date (Date): Fecha del envio
            customer (Customer): Cliente del envio
            shippingNumber (_type_): Numero del envio
            Order (_type_): Orden(Factura) del envio
            shippingService (str): Servicio del envio
            shippingCost (float): Costo del envio
        """        
        self.date=date
        self.customer=customer
        self.shippingNumber=shippingNumber
        self.order=Order
        self.shippingService=shippingService 
        self.shippingCost=shippingCost 
        if shippingService=='Delivery':
            self.delivery=register_delivery()

    def show_atr(self):
        """_Muestra los atributos de una instancia de la clase Shipping
        
        Returns:
            str: --retorna los atributos ordenados de dicha instancia.
            """
        
        if self.shippingService=='Delivery':
            return f'''
        Fecha: {self.date.show_date()}          Numero de envio: {self.shippingNumber}
        Cliente: {self.customer.name}  {self.customer.identifierDocument}
        
        Orden del envio: 
                {self.order.show_atr()}
        
        Metodo de envio: {self.shippingService}
        
        Datos del delivery: {self.delivery.show_atr()}
        
        Metodo de envio: {self.shippingService}

        Costo de envio: {self.shippingCost}
        '''
        else:
            return f'''
        Fecha: {self.date.show_date()}          Numero de envio: {self.shippingNumber}
        Cliente: {self.customer.name}  {self.customer.identifierDocument}
        
        Orden del envio: 
                {self.order.show_atr()}
        
        Metodo de envio: {self.shippingService}
                
        Costo de envio: {self.shippingCost}
        '''
