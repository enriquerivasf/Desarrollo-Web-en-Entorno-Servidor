#Importo el random e inicializo las variables 
import random
cont=0
contador=1
pregunta1=0
pregunta2=0
pregunta3=0



# El while hace que se siga ejecutando el programa hasta que se hagan 2 preguntas 
while contador<=2:
    
    preguntaAleatoria=random.randint(1,3) 
    # Ahora que ya tengo el número random hago un if para que no vuelva a salir esa pregunta
    if(preguntaAleatoria==1):
        pregunta1=pregunta1+1
    elif(preguntaAleatoria ==2):
        pregunta2=pregunta2+1
    elif(preguntaAleatoria==3):
        pregunta3=pregunta3+1
    
    
    # Este if hace que si el número random es 1 y la pregunta 1 aun no ha salido pues que se ejecute(si hubiera salido ya entonces pregunta1 seria igual a 2)
    if(preguntaAleatoria==1 and pregunta1==1):
        print(" ")
        print(" ")
        print("¡Adivina!")
        print("Cual es mi color favorito?")
        print("a) Verde ")
        print("b) Rojo")
        print("c) Morado")

        print(" ")
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
        contador=contador+1 #Con este contador se evita que haya mas de 3 preguntas
            # Este if hace que si el número random es 2 y la pregunta 2 aun no ha salido pues que se ejecute
            
    elif(preguntaAleatoria==2 and pregunta2==1):        
        print(" ")
        print(" ")
        print("¡Adivina!")
        print("Cual es mi serie favorita?")
        print("a) La casa del dragón ")
        print("b) El Señor de los Anillos: los Anillos de Poder")
        print("c) Rick y Morty")

        print(" ")
        respuesta =""
        respuesta = input("Elige una de las opciones(a,b,c): ")

        while(respuesta !="a" and respuesta !="b" and respuesta !="c" ):
            respuesta = input ("Elige una de las opciones(a,b,c): ")# Con este while hago que al poner una letra distinta a las que se piden te vuelva a pedir que elijas una opcion
            
        if respuesta =="a":
            print("Acertaste")
            cont=cont + 10
        else:
            print("Fallaste")
            cont=cont - 5
        contador=contador+1 #Con este contador se evita que haya mas de 3 preguntas
    
    # Este if hace que si el número random es 3 y la pregunta 3 aun no ha salido pues que se ejecute
    elif(preguntaAleatoria==3 and pregunta3==1):     
        print(" ")
        print(" ")
        print("¡Adivina!")
        print("Cuanto es 5+2?")
        print("a) 5 ")
        print("b) 2")
        print("c) 7")

        print(" ")
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
        contador=contador+1 #Con este contador se evita que haya mas de 3 preguntas
    
    # Imprimo la respuesta
print(" ")        
print("En total tienes "+ str(cont) + " puntos")
print(" ")
print(" ")        