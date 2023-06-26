# TODO: "Por hacer" Usar en partes que requieren modificar.

from Date import Date
from Validations import is_float
from Functions import calculate_deadline

prueba=input('Rif')

def is_rif(rif:str): # TODO: "Hacer docsting" #len(rif)==12 #J‑29989842‑2
        if "-" in rif and rif.count("-")==2 and len(rif)==12:
            div=rif.split("-",2)
            if "J" in div[0] and div[1].isnumeric() and len(div[1])==8 and div[2].isnumeric() and len(div[2])==1:
                  return True
        else:
              return False

print(is_rif(prueba))

