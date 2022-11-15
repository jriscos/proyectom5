'''
Modifica el ejercicio 3.4 para que pida la contraseña hasta tres veces, mostrando un mensaje de
error si el usuario se equivoca. Como pista, sigue estos pasos:
a) Primero crea un programa que pida repetidamente la contraseña mientras sea incorrecta.
b) A continuación añade un contador que recuerde cuantas veces se pide la contraseña. Imprime
el número de intentos cuando el usuario acierte.
c) Por último añade a la condición de salida del bucle que si al tercer intento no acertó la
contraseña el programa acabe. Aviso: ten en cuanta que ahora la iteración puede finalizar por
que el usuario acierta la contraseña o por que no la acierta en un número determinado de veces,
y el mensaje a imprimir será diferente en un caso u otro.
'''

contraseña = str(input("Indique la contraseña \n"))
contador = 2

if contraseña == 'iloveyou123':
    print ("Contraseña correcta \n")

while contraseña != 'iloveyou123':
   contraseña = str(input("Contraseña incorrecta \n")) 
   contador = contador + 1

   if contador > 3:
    print ("Fin del programa. \n")
    break

