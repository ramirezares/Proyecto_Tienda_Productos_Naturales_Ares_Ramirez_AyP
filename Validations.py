"""_Archivo que contiene las validaciones_"""

from Date import Date

def is_int(num):
        try:
                int(num)
                return True
        except ValueError:
              return False

def is_float(num):
        try: 
                float(num)
                return True
        except ValueError:
                return False

def is_naturalName(name:str):          #Natural name
      if " " in name and name.count(" ")==1:
        provisional_name=name
        copy=provisional_name.replace(" ","a")
        if copy.isalpha() and len(name)>=3 and len(name)<=30:
            return True
      return False

def is_productName(name):          # Product's name
        if " " in name:
              provisional_name=name
              copy=provisional_name.replace(" ","a")
              if copy.isalpha() and len(name)>=3 and len(name)<=50:
                    return True
        elif type(name)==str:
              provisional_name=name
              if provisional_name.isalpha() and len(provisional_name)>=3 and len(provisional_name)<=50:
                    return True
        return False

def is_description(description:str):
      if " " in description and "," in description or "." in description:
            provisional_description=description.replace(' ','a')
            copy=provisional_description.replace(',','b')
            copy2=copy.replace('.','c')
            if copy2.isalnum() or copy2.isalpha() and len(description)>=15 and not len(description)<=200:
              return True
      return False
      
def is_price(price:str):
      if is_float(price) and len(price)>=1 and len(price)<=4: 
            return True
      return False
      
def is_category(category:str):
      if category.isalpha() and len(category)>=3 and len(category)<=20: 
            return True
      return False
            
def is_availability(availability:str):
      if is_int(availability) and len(availability)>=1 and len(availability)<=4: 
            return True
      return False
      
def is_socialReason(socialReason:str): #Legal name
      if " " in socialReason:
            provisional_socialReason=socialReason
            copy=provisional_socialReason.replace(" ","a")
            copy2=copy.replace(",","b")
            copy3=copy2.replace(".","c")
            if copy3.isalpha() and len(socialReason)>=3 and len(socialReason)<=45:
              return True
      return False


def is_email(email:str):               
        if "@" in email and email.count('@')==1:                            
                div=email.split('@')
                
                before_arroba=div[0]
                count_up = 0
                count_low = 0
                count_num = 0
                for i in before_arroba:
                    if i.isalpha() and i.isupper():
                      count_up += 1
                    if i.isalpha() and i.islower():
                      count_low += 1
                    if i.isnumeric():
                      count_num += 1
                if len(before_arroba)>6 and count_up != 0 and count_low != 0 and count_num != 0: #Al menos una mayuscula, una minuscula, un numero y len>4
                        val_before_arroba=True
                else:
                       val_before_arroba=False

                after_arroba=div[1]
                if 'gmail.com' in after_arroba or 'hotmail.com' in after_arroba: #dominios requeridos
                       val_after_arroba=True
                else:
                       val_after_arroba=False
                
                if val_before_arroba and val_after_arroba:
                       return True
                else:
                      return False
        else:
              return False
        
def is_address(address:str):
        if ' ' in address and ',' in address or '.' in address and len(address)>=35 and len(address)<=100:
              provisional_address=address.replace(' ','a')
              copy=provisional_address.replace(',','b')
              copy2=copy.replace('.','c')
              if copy2.isalnum() or copy2.isalpha():
                  return True
        return False             

def is_phoneNumber(phoneNumber:str): 
    if "." in phoneNumber and phoneNumber.count('.')==1 and len(phoneNumber)==12:
           div=phoneNumber.split('.',1)
           if div[0].isnumeric() and div[1].isnumeric():
                      if len(div[0])==4 and div[0]=="0424" or div[0]=="0414" or div[0]=="0212" or div[0]=="0412" or div[0]=="0426" or div[0]=="0416":
                            return True
    else: 
         return False

def is_cedula(cedula:str):
       if "." in cedula and cedula.count('.')==2 and len(cedula)==9 or len(cedula)==10:
        div=cedula.split('.',2)
        millions=range(1,36)
        if div[0].isnumeric() and div[1].isnumeric() and div[2].isnumeric():
              if int(div[0]) in millions and len(div[0])==1 or len(div[0])==2 and len(div[1])==3 and len(div[2])==3:
                     return True        
        else:
              return False
        

def is_rif(rif:str):  #len(rif)==12 Ej: J‑29989842‑2
        if "-" in rif and rif.count("-")==2 and len(rif)==12:
            div=rif.split("-",2)
            if "J" in div[0] and div[1].isnumeric() and len(div[1])==8 and div[2].isnumeric() and len(div[2])==1:
                  return True
        else:
              return False

def is_date(date:Date): 
        calendary={"1":31,
                   "2":28,
                   "3":31,
                   "4":30,
                   "5":31,
                   "6":30,
                   "7":31,
                   "8":31,
                   "9":30,
                   "10":31,
                   "11":30,
                   "12":31}
        if is_int(date.year) and date.year in range(2000,2051):
              if is_int(date.month) and date.month in range(1,len(calendary)+1):
                    if is_int(date.day) and date.day in range(1,calendary[f'{date.month}']+1):
                          return True
        return False

def is_period_of_one_year(date_init:Date,date_final:Date):
      if int(date_final.year)-int(date_init.year)==1:
            if int(date_final.month)-int(date_init.month)==0:
                  if int(date_final.day)-int(date_init.day)==0:
                        return True
                  else:
                        return False
            else:
                  return False
      else:
            return False
