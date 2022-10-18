import time
from factorial import func_factorial
from factorial2 import func_factorial2

print("a) Calcular el factorial con recursividad ")
print("b) Calcular el factorial sin recursividad")
opcion=input("Elige una opción: ")




if(opcion== "a"):
    start_time = time.time()
    numero=int(input("Introduce un número para calcular el factorial: "))
    print("El factorial del numero "+ str(numero) + " es "+ str(func_factorial(numero)))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('El tiempo de ejecución ha sido :' + str(elapsed_time) + "s")
   
    
if(opcion== "b"):
   
    start_time = time.time()
    numero=int(input("Introduce un número para calcular el factorial: "))
    print("El factorial del numero "+ str(numero) + " es "+ str(func_factorial2(numero)))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('El tiempo de ejecución ha sido :' + str(elapsed_time) + "s")