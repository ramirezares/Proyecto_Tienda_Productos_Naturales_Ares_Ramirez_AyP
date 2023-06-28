# TODO: "Por hacer" Usar en partes que requieren modificar.

from Date import Date
from Validations import is_float
from Functions import calculate_deadline

products=[{"name":'Hola1'},{"name":'Hola2'}]

productName="Hola"

for product in products:
    if product['name']!=productName:
       print('No esta.')
