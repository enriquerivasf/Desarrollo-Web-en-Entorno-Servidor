print("¡Adivina!")
print("Cual es mi color favorito?")
print("a) Verde ")
print("b) Rojo")
print("c) Morado")

respuesta =""

respuesta = input("Elige una de las opciones(a,b,c): ")

while(respuesta !="a" and respuesta !="b" and respuesta !="c" ):
    respuesta = input ("Elige una de las opciones(a,b,c): ")
    
if respuesta =="c":
    print("Acertaste")
else:
    print("Fallaste")
    
        