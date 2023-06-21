# Clase Producto. Atributos: name, description, price:float, category, availability
#                  Metodos: show_atr() , modify_atr(atr)

class Product:
    # TODO: Hacer docstring:
    def __init__(self,name:str, description:str, price:float, category, availability):
        self.name=name
        self.description=description
        self.price=price
        self.category=category
        self.availability=0

    def show_atr(self):
        # TODO: Hacer docstring:
        return f'''
        Nombre: {self.name}
        Descripcion: {self.description}
        Precio: {self.price}
        Categoria: {self.category}
        Disponibilidad: {self.availability}
        '''

    def modify_atr(self,atr_number):
        # TODO: Hacer docstring:
        if atr_number=='1':
            new_name=input('Introduzca el nuevo nombre:')
            while not len(new_name)<=30: 
                new_name=input('Invalido. Introduzca el nuevo nombre:')
            self.name=new_name
            print('Cambios guardados.')

        if atr_number=='2':
            new_description=input('Introduzca la nueva descripcion:')
            while len(new_description)<=200: 
                new_description=input('Invalido. Introduzca la nueva descripcion:')
            self.description=new_description
            print('Cambios guardados.')

        if atr_number=='3':
            new_price=input('Introduzca el nuevo precio:')
            #while #is_float and len(new_description)<=200: 
            #    new_description=input('Invalido. Introduzca la nueva descripcion:')
            self.price
            print('Cambios guardados.')
        
        if atr_number=='4':
            new_category=input('Introduzca la nueva categoria:')
            while len(new_category)<=15: 
                new_category=input('Invalido. Introduzca la nueva categoria:')
            self.category=new_category
            print('Cambios guardados.')
        
        #if atr_number=='5':
        #    self.availability=input('Introduzca la disponibilidad:') 
        #TODO: Preguntar a Paola 
        
