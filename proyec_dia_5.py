from random import *
def letra_correcta():
    print(f" La letra {letra} esta en la palabra secreta")
    for i in range(len(seleccion)):
        if seleccion[i]== letra:
            palabra_oculta[i]= letra
def letra_incorrecta():
    if intentos >0:
            print(f'La letra "{letra}" no esta en la palabra, te quedan {intentos} intentos')
    elif intentos<1:
            juego =False
            print(f'La leltra "{letra}" no esta en la palabra')
            print("Se terminaron tus intentos y no has adivinado la palabra")
    
    
lista_palabras = ["teclado", "televsor", "gaviota","almohada", "universidad", "analista", "estufa","cemento"]
seleccion = choice(lista_palabras)
palabra_oculta = ['*' for _ in seleccion]
print("Tienes 5 oportunidades para adivinar la palabra.")
letra = "a"
juego = True
intentos = 5
while juego:
    print("".join(palabra_oculta))
    valor = 0
    print("Ahora, ingresa una letra:")
    letra = input("")
    if letra in seleccion:
        letra_correcta()
    elif letra not in seleccion:
        intentos = intentos - 1
        letra_incorrecta()
    if '*' not in palabra_oculta:
        print(f"Has adivinado la palabra, ganaste, era {''.join(palabra_oculta)}")
        juego = False
    if intentos<1:
        juego = False