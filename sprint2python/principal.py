from factorial import func_factorial
from factorial2 import func_factorial2

print("a) Calcular el factorial con recursividad ")
print("b) Calcular el factorial sin recursividad")
opcion=input("Elige una opción: ")




if(opcion== "a"):
    numero=int(input("Introduce un número para calcular el factorial: "))
    print("El factorial del numero "+ str(numero) + " es "+ str(func_factorial(numero)))
if(opcion== "b"):
    
    numero=int(input("Introduce un número para calcular el factorial: "))
    print("El factorial del numero "+ str(numero) + " es "+ str(func_factorial2(numero)))