def func_factorial2(numero):
    if numero==0 or numero==1:
            numero=1
    else: 
        factorial = 1
        while(numero > 1): 
            factorial *= numero 
            numero -= 1
        return factorial 
