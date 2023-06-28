# Class Pay. Atr: costumer, total, paymentCurrency, paymentType, date, payNumber, payStatus
#           Metodos: Show_atr
from Date import Date

from Customer import Customer
class Pay:
    # TODO: Hacer docstring:
    def __init__(self,date:Date,payNumber:str,customer:Customer,paymentType:str,paymentCurrency:str,total:float,payStatus:str):
        self.date=date              #Cambiar el orden en el diagrama
        self.payNumber=payNumber
        self.customer=customer
        self.paymentType=paymentType
        self.paymentCurrency=paymentCurrency
        self.total=total
        self.payStatus=payStatus

    def show_atr(self):
        # TODO: Hacer docstring:
        return f'''
        Fecha: {self.date.show_date()}      Numero de pago: {self.payNumber}
        Cliente: {self.customer.name} Cedula o RIF:{self.customer.identifierDocument}
        Tipo de pago: {self.paymentType}    Moneda de pago: {self.paymentCurrency}
        Monto total: {self.total}
        Estado de pago: {self.payStatus}
        '''                                 #Cambiar el orden en el diagrama