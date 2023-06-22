from Validations import is_email
from Validations import is_phoneNumber
from Validations import is_cedula
from Customer import Customer

class Natural(Customer):
    """_Clientes de la clase Natural que son registrados e interactuan en la Tienda_

    Methods:
        show_atr: str
        modify_atr: void

    La clase 'Natural' hereda el comportamiento de la clase Cliente 'Customer'.
    La clase Natural varia en que agrega dos (2) atributos: lastName y identifierDocument.
    """

    def __init__(self,name:str,email:str,address:str,phoneNumber:str,lastName:str,identifierDocument:str):
        """_Crea una instancia de la clase Natural _

        Args:
            name (str): --El nombre del cliente Natural.
            email (str): --El correo del cliente Natural.
            address (str): --La direccion del cliente Natural.
            phoneNumber (str): --El numero de telefono del cliente Natural.
            lastName (str): --El apellido del cliente Natural.
            identifierDocument (str): --La cedula del cliente Natural.
        
        La superclase 'Customer' extiende su constructor y la subclase Natural adiciona al metodo constructor para conformar el suyo.       
        """
          
        super().__init__(name,email,address,phoneNumber)
        self.lastName=lastName
        self.identifierDocument=identifierDocument

    def show_atr(self):
        """_Muestra los atributos de una instancia de la clase Natural_

        Args:
        self -- la instancia, preteneciente a la clase Natural, de la cual se desea visualizar los atributos.

        Returns:
            str: --retorna los atributos ordenados de dicha instancia.

        La subclase 'Natural' anula el metodo del mismo nombre de la superclase 'Customer'.
        Lo hace para remplazar el metodo pero mantiene el mismo comportamiento, solo que integrando los nuevos atributos.
        """

        return f'''
        Nombre: {self.name}
        Apellido: {self.lastName}
        Email: {self.email}
        Direccion: {self.address}
        Numero de telefono: {self.phoneNumber}
        Cedula: {self.identifierDocument}
        '''
    
    def modify_atr(self,atr_number):
        """_Modifica los atributos de una instancia de la clase Cliente

        Args:
            atr_number (int): _Representa el numero del atributo que se desea modificar, en el orden mostrado en el __init__.

        La subclase 'Natural' anula el metodo del mismo nombre de la superclase 'Customer'.
        Lo hace para remplazar el metodo pero mantiene el mismo comportamiento, solo que integrando los nuevos atributos.
        """

        if atr_number=='1':         #name
            new_name=input('Introduzca el nuevo nombre:')
            while not new_name.isalpha() and not len(new_name)>=3 and not len(new_name)<=45 and not " " in new_name:    #cortar
                new_name=input('Invalido. Introduzca el nuevo nombre:')
            self.name=new_name
            print('Cambios guardados.')

        if atr_number=='2':         #email
            new_email=input('Introduzca el nuevo correo:') 
            while not is_email(new_email):
                new_email=input('Invalido. Introduzca el nuevo correo:')
            self.email=new_email
            print('Cambios guardados.')

        if atr_number=='3':         #address
            new_address=input('''
            Introduzca la nueva direccion(Ciudad,Urbanizacion,Casa.Estado):''')
            while not ',' in new_address and not '.' in new_address and not len(new_address)>=35 and not len(new_address)<=150:
                new_address=input('''
            Introduzca la nueva direccion(Ciudad,Urbanizacion,Casa.Estado):''')
            self.address=new_address
            print('Cambios guardados.')
        
        if atr_number=='4':         #phoneNumber
            new_phoneNumber=input('Introduzca el nuevo numero de telefono con un solo punto: (Ej: 0412.2972606)')
            while not is_phoneNumber(new_phoneNumber): 
                new_phoneNumber=input('Invalido. Introduzca el nuevo numero de telefono:')
            self.category=new_phoneNumber
            print('Cambios guardados.')

        if atr_number=='5': #lastName
            new_lastName=input('Introduzca el nuevo apellido:')
            while not new_lastName.isalpha() and not len(new_lastName)>=2 and not len(new_lastName)<=45 and not " " in new_lastName:
                new_lastName=input('Invalido. Introduzca el nuevo apellido:')
            self.lastName=new_lastName
            print('Cambios guardados.')

        if atr_number=='6': #identifierDocument
            new_identifierDocument=input('Introduzca la nueva cedula:')
            while not is_cedula(new_identifierDocument):
                new_identifierDocument=input('Invalido. Introduzca la nueva cedula:')
            self.identifierDocument=new_identifierDocument
            print('Cambios guardados.')
         
        
