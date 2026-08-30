txt=[0] * 10000
def menu():
    print("                                                   py os hecho por David Agustín González Gimeno")
    print("c=abre una calculadora  nuevo=crea un archivo  abrir=abre un archivo  formatear=borra todos los archivos ayuda=comandos disponibles")
      
menu()
def c():
    print("[---------------]")
    print("[  CALCULADORA  ]")
    print("[_______________]")
    print("[ 1     2    3  ]")
    print("[ 4     5    6  ]")
    print("[ 7     8    9  ]")
    print("[ 0     +    -  ]")
    print("[ *     /    %  ]")
    print("[               ]")
    print("[_______________]")
    e=float(input("primer dígito: "))
    x=float(input("segundo dígito: "))
    print("suma: ",e + x)
    print("resta: ",e - x)
    print("mutiplicación: ",e * x)
    print("división: ",e / x)
    

        
def abrir(digit):
    if txt[digit] == 0:
        print("no se encuentra el archivo pruebe con otro digito de archivo ")
    else:
        print(txt[digit])
        

def nuevo(num):
    ml=input("escribe el texto: ")
    txt[num]=ml
    print(ml)
    

def formatear():
    wi=input("Estas seguro?[SI]o[NO]")
    if wi=="SI":
        txt=[0] * 10000
        menu()
def borrar():
  ire=int(input("ID del archivo que desea borrar: "))
  txt[ire]=0
   
  
while True:
    en=input("usuario@AgusOS(Núcleo)#")
    if en=="c":
        c()
    elif en=="abrir":
        rie=int(input("ID del archivo que desea abrir: "))
        abrir(rie)
    elif en=="formatear":
        formatear()
    elif en=="nuevo":
        yu=int(input("ID del nuevo archivo: "))
        nuevo(yu)
    elif en=="ayuda":
        menu()
    elif en=="borrar":
      borrar()
      