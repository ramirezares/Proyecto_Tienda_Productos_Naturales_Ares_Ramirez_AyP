# Class Pay. Atr: costumer, total, paymentCurrency, paymentType, date, payNumber, payStatus
#           Metodos: Show_atr
from Costumer import Costumer
class Pay():
    def __init__(self,costumer:Costumer,total:float,paymentCurrency:str,paymentType:str,date:str,payNumber:str,payStatus:str):
        self.date=date              #Cambiar el orden en el diagrama
        self.payNumber=payNumber
        self.costumer=costumer
        self.paymentType=paymentType
        self.paymentCurrency=paymentCurrency
        self.total=total
        self.payStatus=payStatus

    def show_atr(self):
        return f'''
        Fecha: {self.date}
        Numero de pago: {self.payNumber}
        Cliente: {self.costumer}
        Tipo de pago: {self.paymentType}
        Moneda de pago: {self.paymentCurrency}
        Monto total: {self.total}
        Estado de pago: {self.payStatus}
        '''                                 #Cambiar el orden en el diagrama