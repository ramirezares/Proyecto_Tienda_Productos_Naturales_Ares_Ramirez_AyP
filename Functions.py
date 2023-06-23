from Date import Date
# TODO: Funcion de imprimir menu recibe una lista y un numero

def print_options(options:list):
        """_summary_ # TODO: "Completar"

        Args:
            options (list): _Lista de la cual se desea imprimir las opciones_
        """      
        for i in range(len(options)):
                    print(f'{i+1}. {options[i]}')

def calculate_deadline(actual_date:Date,amount_of_days:int):
        if actual_date.month==1:   #enero
            num_of_Day_of_month=31
            deadline_date=None          #requiere los 3 nuevos atributos
            actualDay=actual_date.day
            last_pay_day=actualDay+amount_of_days
            pay_month=actual_date.month
            pay_year=actual_date.year
            if last_pay_day>num_of_Day_of_month:
                last_pay_day-=num_of_Day_of_month
                pay_month+=1
            deadline_date=Date(last_pay_day,pay_month,pay_year)
            return deadline_date

        if actual_date.month==2:   #febrero #implementar en cada mes
            num_of_Day_of_month=28

        if actual_date.month==3:   #marzo
            num_of_Day_of_month=31

        if actual_date.month==4:   #abril
            num_of_Day_of_month=30

        if actual_date.month==5:   #mayo
            num_of_Day_of_month=31

        if actual_date.month==6:   #junio
            num_of_Day_of_month=30
        if actual_date.month==7:   #julio
            num_of_Day_of_month=31
        if actual_date.month==8:   #agosto
            num_of_Day_of_month=31
        if actual_date.month==9:   #septiembre
            num_of_Day_of_month=30
        if actual_date.month==10:   #octube
            num_of_Day_of_month=31
        if actual_date.month==11:   #noviembre
            num_of_Day_of_month=30
        if actual_date.month==12:   #diciembre
            num_of_Day_of_month=31

            
    
    