
print('''         ⒿⓊⒺⒼⓄ ⓅⒾⒺⒹⓇⒶ ⓅⒶⓅⒺⓁ ⓉⒾⒿⒺⓇⒶⓈ
                        By: Jrules''')
print('''                        cargando...''')
import time
time.sleep(1)
print("Para jugar seleccione si quiere ser piedra,papel o tijeras")
while True:
    
 print(''' PIEDRA  --> 1
 PAPEL   --> 2
 TIJERAS --> 3''')
 x=input("-->")
 y=float(x)
 import random
 numero_aleatorio = random.randint(1, 3)
 numrndm= float(numero_aleatorio)
 if(numrndm==1):
     print("BOT USO PIEDRA")
 elif(numrndm==2):
     print("BOT USO PAPEL")
 elif(numrndm==3):
     print("BOT USO TIJERA")

 if(numrndm==1) and (y==1):
  print("empate")
 elif(numrndm==2) and (y==2):
  print("empate")
 elif(numrndm==3) and (y==3):
  print("empate")
 elif(numrndm==3) and (y==1):
  print("ganas")
 elif(numrndm==1) and (y==3):
  print("pierdes")
 elif(numrndm==2) and (y==1):
  print("pierdes")
 elif(numrndm==1) and (y==2):
  print("ganas")
 elif(numrndm==3) and (y==2):
  print("pierdes")
 elif(numrndm==2) and (y==3):
  print("ganar")
 elif(numrndm==2) and (y==1):
  print("pierdes")
 elif(numrndm==1) and (y==2):
  print("ganar")
 else:(print("SELECCIONE OTRA OPCION"))
 

        
 
