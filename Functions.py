# TODO: Funcion de imprimir menu recibe una lista y un numero

def print_options(options:list):
        """_summary_ # TODO: "Completar"

        Args:
            options (list): _Lista de la cual se desea imprimir las opciones_
        """      
        for i in range(len(options)):
                    print(f'{i+1}. {options[i]}')

