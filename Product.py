from Functions import is_float
from Functions import is_int

class Product:
    """_Productos que son vendidos e interactuan en la Tienda_

    Methods:
        show_atr: str
        modify_atr: void
    """
    
    def __init__(self,name:str, description:str, price:float, category:str):
        """_Crea una instancia de la clase Producto_

        Args:
            name (str): --El nombre del producto
            description (str): --La descripcion del producto
            price (float): --El precio del producto
            category (str): --La categoria del producto     #TODO Ver si el profe cambia la API y pone availavility
        """

        self.name=name
        self.description=description
        self.price=price
        self.category=category
        self.availability=10

    def show_atr(self):
        """_Muestra los atributos de una instancia de la clase Producto_

        Args:
        self -- la instancia, preteneciente a la clase productos, de la cual se desea visualizar los atributos.

        Returns:
            str: --retorna los atributos ordenados de dicha instancia
        """

        return f'''
        Nombre: {self.name}
        Descripcion: {self.description}
        Precio: {self.price}
        Categoria: {self.category}
        Disponibilidad: {self.availability}
        '''

    def modify_atr(self,atr_number):
        """_Modifica los atributos de una instancia de la clase Producto_

        Args:
            atr_number (int): _Representa el numero del atributo que se desea modificar, en el orden mostrado en el __init__.
        """

        if atr_number=='1':         #name
            new_name=input('Introduzca el nuevo nombre:')
            while not new_name.isalpha() and not len(new_name)>=3 and not len(new_name)<=30:
                new_name=input('Invalido. Introduzca el nuevo nombre sin numeros:')
            self.name=new_name
            print('Cambios guardados.')

        if atr_number=='2':         #description
            new_description=input('Introduzca la nueva descripcion:') 
            while not len(new_description)>=15 and not len(new_description)<=200:
                new_description=input('Invalido. Introduzca la nueva descripcion:')
            self.description=new_description
            print('Cambios guardados.')

        if atr_number=='3':         #price
            new_price=input('Introduzca el nuevo precio:')
            while not is_float(new_price) and not len(new_price)>=1 and not len(new_price)<=5: 
                new_price=input('Invalido. Introduzca el nuevo precio:')
            self.price=new_price
            print('Cambios guardados.')
        
        if atr_number=='4':         #category
            new_category=input('Introduzca la nueva categoria:')
            while not new_category.isalpha() and not len(new_category)>=3 and not len(new_category)<=20: 
                new_category=input('Invalido. Introduzca la nueva categoria:')
            self.category=new_category
            print('Cambios guardados.')
        
        if atr_number=='5':         #availavility
            new_stock=input('Introduzca la nueva disponibilidad:')
            while not is_int(new_stock) and not len(new_stock)>=1 and not len(new_stock)<=5: 
                new_stock=input('Invalido. Introduzca la nueva disponibilidad:')
            self.availability=new_stock
            print('Cambios guardados.')
         
        
