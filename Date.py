#TODO - Hacer Docstrings
class Date:
    def __init__(self,day:int,month:int,year:int):
        self.day=day
        self.month=month
        self.year=year

    def show_date(self):
        return f"{self.day}/{self.month}/{self.year}"
    
    