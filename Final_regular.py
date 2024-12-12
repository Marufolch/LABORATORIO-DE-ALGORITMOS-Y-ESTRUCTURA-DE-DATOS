# Ejercicios 1
# Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:
# La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).
# Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.
# Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función 
# deberecibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:
# Si la suma es menor o igual a 6:
# "La suma de tus dados es {suma_dados}. Lamentable"
# Si la suma es mayor a 6 y menor a 10:
# "La suma de tus dados es {suma_dados}. Tienes buenas chances"
# Si la suma es mayor o igual a 10:
# "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
# Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6
print('******** 1-Ejercicio Dados***************')
from random import randint
def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return dado1, dado2

def evaluar_jugada(dado1, dado2):
    suma_dado = dado1 + dado2
    if suma_dado <= 6:
        return(f'la suma de tus dados es {suma_dado}. Lamentable')
    elif 10> suma_dado > 6:
        return(f'La suma de tus dados es {suma_dado}. Tienes buenas chances.')
    else:
        return(f'La suma de tus dados es {suma_dado}. Parece una jugada ganadora')

dado1,dado2 =lanzar_dados() #llamo a las variables 
print(evaluar_jugada(dado1,dado2)) #imprimo para ver si funciona

# Ejercicio 2
# Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder 
# devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.
# Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de 
# la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).
print('****** 2-Ejercicio moneda*******')
from random import choice
def lanzar_moneda():
    opcion = choice(['cara', 'cruz'])
    return opcion
#lanzar_moneda()

lista_numeros= [1,23,24,12,5]
def probar_suerte(lado, lista):
    lista
    if lado == 'cara':
        print('La ista se auto destruira')
        lista.clear()
        return lista
    else:
        print('la lista fue salvada')
        return lista
opcion= lanzar_moneda() #llamo la variable
print(probar_suerte(opcion, lista_numeros)) #impromo para ver si funciona

# Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).
# Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.
# Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.



# Ejercicio 3
# Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando 
# sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.

print('***** 3-Ejercicio suma menores*******')
lista_numeros2 = [-22,500,1001,150]
def suma_menores(lista):
    total = 0
    for numero in lista:
        if 1000 > numero > 0:
            total += numero
    return total
print(suma_menores(lista_numeros2))

# Ejercicio 4
# Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de defensa específicos.
# Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia de las clases de tus personajes), y 
# ejecutar su método defender() independientemente de qué tipo de personaje se trate.
print('******** 4- ejercicio defender***********')
class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

mago1= Mago()
arquero1= Arquero()
samurai1= Samurai()

def personaje_defender(defenza):
    defenza.defender()

personaje_defender(samurai1) #llamo para ver si funciona
personaje_defender(arquero1)
personaje_defender(mago1)

# Ejercicio 5
# Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:
# real = False
# Crea una instancia llamada harry_potter con los siguientes atributos de instancia:
# especie = "Humano"
# magico = True
# edad = 17

class Personaje():
    real= False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad
    
harry_potter = Personaje('humano', True, 17) #especificamos los atributos de Harry
print(harry_potter.edad)#imprimo para ver si funciona
print(harry_potter.especie)
print(harry_potter.magico)