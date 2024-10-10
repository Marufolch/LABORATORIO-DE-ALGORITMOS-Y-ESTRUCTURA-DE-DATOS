print("Hola! Tengo un pequeño juego para ti. Pero primero ¿Como te llamas?")
#nombre = input("ingrese aqui su nombre: ")
#print(f"Bueno {nombre}, ahora podemos empezar. El juego se trata de que adivines un numero entero del 1 al 100 que he elegido al azar")
print('Tendras solo 8 intentos. Suerte!')
from random import *

numero = randint(1,100)
intentos = 8
print(numero)
adivinar = int(input("ingresa el numero: "))
while adivinar != numero:
    if adivinar <= 0 or adivinar >=100:
        print('Debes ingresar un numero del 1 al 100')
        intentos += -1
        print(f'te quedan {intentos} intentos')
        adivinar = int(input("ingresa el numero nuevamente: "))
    elif adivinar > 0 and adivinar < numero:
        print("Es incorrecto, intenta de nuevo")
        intentos += -1
        print(f'te quedan {intentos} intentos')
        print('pero aqui tienes un pista: ')
        print("el numero que quieres adivinar es mayor")
        adivinar = int(input("ingresa el numero nuevamente: "))
    elif adivinar > numero and adivinar <100:
        print("Es incorrecto, intenta de nuevo")
        intentos += -1
        print(f'te quedan {intentos} intentos')
        print('pero te doy una pista: ')
        print('el numero que quieres adivinar es menor')
        adivinar = int(input("ingresa el numero nuevamente: "))
    if intentos == 1:
        print("se terminaron los intentos, lo siento no has adivinado")
        break 
if adivinar == numero:
    print('has acertado! Felicitaciones')
   # except:
        #print("error, debes ingresar un dato numerico")