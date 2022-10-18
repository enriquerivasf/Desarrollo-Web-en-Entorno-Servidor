def func_factorial(numero):
    if numero==0 or numero==1:
            numero=1
    elif numero>1:
            numero=numero*func_factorial(numero-1)
    return numero
