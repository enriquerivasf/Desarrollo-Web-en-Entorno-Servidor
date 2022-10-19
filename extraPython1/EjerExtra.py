import random

opcionJugador = 0
opcionMaquina = 0
cont = 0
puntuacionJugador = 0
puntuacionMaquina = 0
while cont < 5:
    opcionJugador= int(input("Elige una opcion (1,2,3) \n 1)piedra \n 2)papel \n 3)tijera \n  "))
    print(" ")
    if(opcionJugador==1 or opcionJugador==2 or opcionJugador==3):

        opcionMaquina = random.randint(1, 3)

        if (opcionJugador==1 and opcionMaquina==1):
            print("Empate")
            cont = cont + 1

        elif (opcionJugador==1 and opcionMaquina==2):
            print("Has perdido, piedra pierde contra papel ")
            cont = cont + 1
            puntuacionMaquina = puntuacionMaquina + 1

        elif (opcionJugador == 1 and opcionMaquina == 3):
            print("Has ganado, piedra gana a tijera")
            cont = cont + 1
            puntuacionJugador = puntuacionJugador + 1

        elif(opcionJugador == 2 and opcionMaquina == 1):
            print("Has ganado, papel gana a piedra")
            cont = cont + 1
            puntuacionJugador = puntuacionJugador + 1

        elif(opcionJugador == 2 and opcionMaquina == 2):
            print("Empate")
            cont = cont + 1


        elif (opcionJugador == 2 and opcionMaquina == 3):
            print("Has perdido, papel pierde contra tijera")
            cont = cont + 1
            puntuacionMaquina = puntuacionMaquina + 1

        elif(opcionJugador == 3 and opcionMaquina == 1):
            print("Has perdido, tijera pierde contra piedra")
            cont = cont + 1
            puntuacionMaquina = puntuacionMaquina + 1
        
        elif(opcionJugador == 3 and opcionMaquina == 2):
            print("Has ganado, tijera gana contra papel")
            cont = cont + 1
            puntuacionJugador = puntuacionJugador + 1
        
        elif(opcionJugador == 3 and opcionMaquina == 3):
            print("Empate")
            cont = cont + 1
        print(" ")
        print("Jugador: " + str(puntuacionJugador) + " | " + "Maquina: "+ str(puntuacionMaquina))   
        print(" ")
    else :
        print("No has escogido una opción válida")
        print(" ")
if(puntuacionJugador>puntuacionMaquina):
    print(" ")
    print("Felicidades, has ganado")
else:
    print(" ")
    print("Lo siento, has perdido")
    
