# TODO: Funcion de imprimir menu recibe una lista y un numero

def print_options(options:list):
    for i in range(len(options)):
                print(f'{i+1}. {options[i]}')

def is_int(num):
        try:
                int(num)
                return True
        except:
                return False

def is_float(num):
        try: 
                float(num)
                return True
        except:
                return False
        
def is_email(email):
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
                

def in_range(list):
        pass
