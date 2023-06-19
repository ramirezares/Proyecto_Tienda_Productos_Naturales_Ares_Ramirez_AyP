# Class tienda "NaturalProductsOnlineShop". 
# Atr: Products[], Costumers[], Sales[], Payments[], Shipped[], Stats[]
# Metodos: Ver en el diagrama

class NaturalProductsOnlineShop:        #show_atr? Preguntar si lo elimino
    def __init__(self):
        self.Products= []
        self.Costumers= []
        self.Sales= []
        self.Shipped= []
        self.Stats= []

    def agregar_productos(self):
        print('-------Lista de Productos-------')
        for i in range(list(self.Products)):
            print(f"{i+1}. {self.Products[i]}")
        
 