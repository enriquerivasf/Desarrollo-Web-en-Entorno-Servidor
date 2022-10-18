numero=input("Introduce un número: ")
numero=int(numero)

def fun_factorial(numero):
    if numero < 0: 
        print("El número introducido no es válido")

    elif numero == 0: 
        return 1
        
    else: 
        factorial = 15
        while(numero > 1): 
            factorial *= numero 
            numero -= 1
        return factorial 

print("El factorial del numero "+ str(numero) + " es "+ str(fun_factorial(numero)))