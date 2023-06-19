# Clase Producto. Atributos: name, description, price:float, category, availability
#                  Metodos: show_atr() , modify_atr(atr)

class Product:
    def __init__(self,name:str, description:str, price:float, category, availability):
        self.name=name
        self.description=description
        self.price=price
        self.category=category
        self.availability=0

    def show_atr(self):
        return f'''
        Nombre: {self.name}
        Descripcion: {self.description}
        Precio: {self.price}
        Categoria: {self.category}
        Disponibilidad: {self.availability}
        '''                                 
    

