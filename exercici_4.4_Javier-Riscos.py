'''
Crea un programa llamado ex_4_4, que calcule el factorial de un número entero introducido por
el usuario. El número introducido por el usuario debe ser más grande que 0 y más pequeño que
20. Si no fuera así, el programa debe pedirlo de nuevo tantas veces como sea necesario.
Recuerda que el factorial de un número entero es dicho número multiplicado por todos sus
antecesores:
n ! = n × (n – 1) × (n – 2) × ... × 1
'''

while True:
    n = int(input("Introduzca un numero comprendido entre 0 y 20 \n"))

    if n > 20 or n < 0:
        print ("El nombre tiene que estar comprendido entre 0 y 20")
    else: 
        while n >= 1 and n <= 20:
            for i in range (1, n, +1):
                factorial = n * (n - 1)
                print ("El factorial de" , n , "és" , factorial)
                break 
            break
