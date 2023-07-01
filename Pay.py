from Date import Date
from Customer import Customer
class Pay:
    """_Pagos que recibira la tienda en su actividad y seran registrados en respuesta a las ventas_

    Methods:
        show_atr: str
    """

    def __init__(self,date:Date,payNumber:str,customer:Customer,paymentType:str,paymentCurrency:str,total:float):
        self.date=date
        self.payNumber=payNumber
        self.customer=customer
        self.paymentType=paymentType
        self.paymentCurrency=paymentCurrency
        self.total=total

    def show_atr(self):
        """_Muestra los atributos de una instancia de la clase Pay_

        Returns:
            str: --retorna los atributos ordenados de dicha instancia
        """
        return f'''
        Fecha: {self.date.show_date()}                          Numero de pago: {self.payNumber}
        Cliente: {self.customer.name}.          Cedula o RIF: {self.customer.identifierDocument}
        Tipo de pago: {self.paymentType}    Moneda de pago: {self.paymentCurrency}
        Monto total: {self.total}
        '''