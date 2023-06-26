from Validations import is_int
from Validations import is_productName
from Validations import is_description
from Validations import is_price
from Validations import is_category
from Validations import is_availability

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
            new_name=input('Introduzca el nuevo nombre del producto:')
            while not is_productName(new_name):
                new_name=input('Invalido. Introduzca el nuevo nombre del producto:')
            self.name=new_name
            print('Guardado.')

        if atr_number=='2':         #description
            new_description=input('Introduzca la nueva descripcion del producto:') 
            while not is_description(new_description):
                new_description=input('Invalido. Introduzca la nueva descripcion del producto:')
            self.description=new_description
            print('Guardado.')

        if atr_number=='3':         #price
            new_price=input('Introduzca el nuevo precio del producto:')
            while not is_price(new_price):
                new_price=input('Invalido. Introduzca el nuevo precio del producto:')
            self.price=new_price
            print('Guardado.')
        
        if atr_number=='4':         #category
            new_category=input('Introduzca la nueva categoria del producto:')
            while not is_category(new_category):
                new_category=input('Invalido. Introduzca la nueva categoria del producto:')
            self.category=new_category
            print('Guardado.')
        
        if atr_number=='5':         #availavility
            new_stock=input('Introduzca la nueva disponibilidad del producto:')
            while not is_availability(new_stock):
                new_stock=input('Invalido. Introduzca la nueva disponibilidad del producto:')
            self.availability=new_stock
            print('Guardado.')
         
        
