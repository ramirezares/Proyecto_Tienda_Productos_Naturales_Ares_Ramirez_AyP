"""_Archivo que contiene las validaciones
"""

def is_int(num):
        # TODO: "Hacer docsting"
        try:
                int(num)
                return True
        except ValueError:
              return False

def is_float(num):
        # TODO: "Hacer docsting"
        try: 
                float(num)
                return True
        except ValueError:
                return False
        
def is_email(email):
        # TODO: "Hacer docsting"
        if not "@" in email and not email.count('@')==1:
                return False
        if "@" in email and email.count('@')==1:
                for l in range(len(email)):
                        if email[l]=='@':
                                arb=l
                                before_arroba=email[0,arb]
                                val_before_arroba=None
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
                                if len(before_arroba)<=4 or count_up == 0 or count_low == 0 or count_num == 0: #Al menos una mayuscula, una minuscula, un numero y len>4
                                        val_before_arroba=False
                                else:
                                       val_before_arroba=True
                                after_arroba=email[arb,-1]
                                val_after_arroba=None
                                if not "gmail.com" in after_arroba or not "hotmail.com": #dominios requeridos
                                       val_after_arroba=False
                                else:
                                       val_after_arroba=True
                                
                                if val_before_arroba and val_after_arroba:
                                       return True
                                else:
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
       if "." in cedula and cedula.count('.')==2 and len(cedula)==7 or len(cedula)==8:
        div=cedula.split('.',2)
        millions=range(1,36)
        if div[0].isnumeric() and div[1].isnumeric() and div[2].isnumeric():
               if div[0] in millions and len(div[0])==1 or len(div[0])==2 and len(div[1])==3 and len(div[2])==3:
                return True        
        else:
              return False
        

def is_rif(rif:str): # TODO: "Hacer docsting" #len(rif)==9 #J‑29989842‑2
        if "-" in rif and rif.count("-")==2 and len(rif)==12:
            div=rif.split("-",2)
            if "J" in div[0] and div[1].isnumeric() and len(div[1])==8 and div[2].isnumeric() and len(div[2])==1:
                  return True
        else:
              return False

def in_range(list): # TODO: "Hacer docsting"
        pass

