class Date:
    """_Fechas que seran registradas para la actividad de la tienda_
    """    
    def __init__(self,day:int,month:int,year:int):
        self.day=day
        self.month=month
        self.year=year

    def show_date(self):
        """_Muestra la fecha ordenada en dia/mes/año_

        Returns:
            str: --retorna los atributos ordenados de dicha instancia
        """        
        return f"{self.day}/{self.month}/{self.year}"
    
    
    