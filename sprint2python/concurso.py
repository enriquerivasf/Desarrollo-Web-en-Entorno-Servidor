print(" ")
print(" ")
print("¡Adivina!")
print("Cual es mi color favorito?")
print("a) Verde ")
print("b) Rojo")
print("c) Morado")

respuesta =""
cont=0

respuesta = input("Elige una de las opciones(a,b,c): ")

while(respuesta !="a" and respuesta !="b" and respuesta !="c" ):
    respuesta = input ("Elige una de las opciones(a,b,c): ")
    
if respuesta =="c":
    print("Acertaste")
    cont=cont + 10
else:
    print("Fallaste")
    cont=cont - 5
    print(" ")
    print(" ")
print("¡Adivina!")
print("Cual es mi serie favorita?")
print("a) La casa del dragón ")
print("b) El Señor de los Anillos: los Anillos de Poder")
print("c) Rick y Morty")

respuesta =""

respuesta = input("Elige una de las opciones(a,b,c): ")

while(respuesta !="a" and respuesta !="b" and respuesta !="c" ):
    respuesta = input ("Elige una de las opciones(a,b,c): ")
    
if respuesta =="a":
    print("Acertaste")
    cont=cont + 10
else:
    print("Fallaste")
    cont=cont - 5
    
print(" ")
print(" ")
print("¡Adivina!")
print("Cuanto es 5+2?")
print("a) 5 ")
print("b) 2")
print("c) 7")

respuesta =""

respuesta = input("Elige una de las opciones(a,b,c): ")

while(respuesta !="a" and respuesta !="b" and respuesta !="c" ):
    respuesta = input ("Elige una de las opciones(a,b,c): ")
    
if respuesta =="c":
    print("Acertaste")
    cont=cont + 10
else:
    print("Fallaste") 
    cont=cont - 5   
    
print("Has conseguido "+ str(cont) + " puntos")
print(" ")
print(" ")