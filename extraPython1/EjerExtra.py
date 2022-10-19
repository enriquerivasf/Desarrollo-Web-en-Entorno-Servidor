import random

opcionJugador = 0
opcionMaquina = 0
cont = 0
puntuacionJugador = 0
puntuacionMaquina = 0
while cont < 5:
    opcion = input("Que vas a sacar??\n 1)piedra\n papel=2, tijera=3")
    while (opcion != 1 and opcion != 2 and opcion != 3):
        opcionJugador = input("Que vas a sacar??\n 1)piedra\n 2)papel=2\n 3)tijera=3\n")

    opcionMaquina = random.randint(1, 3)

    if (opcionJugador == 1 and opcionMaquina == 1):
        print("Empate")
        cont = cont + 1

    elif (opcionJugador == 1 and opcionMaquina == 2):
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

    print("Jugador: "+ puntuacionJugador + " | "+ puntuacionMaquina)   

