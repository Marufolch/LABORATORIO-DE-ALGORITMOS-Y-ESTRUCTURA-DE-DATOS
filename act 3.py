mi_texto ="Esta noche salgo"
#          ||||||||||||||||
#          0123456789......
resultado = mi_texto[0]
resultado1 = mi_texto[-1]
resultado2 = mi_texto.index("o")
resultado3 = mi_texto.index("h",3,11)
resultado4 = mi_texto.rindex("o")
resultado5 = len(mi_texto)
resultado6 = mi_texto.count("o")

palabra = "ordenador"
#print(palabra[5])
frase = "En teoría, la teoría y la practica son los mismos. En la practica, no lo son."
#print(frase.rindex("practica"))
frase1 = "Controlar la complejidad es la esencia de la programación"
#print(frase1[0:9])
frase2 = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
#print(frase2[9: :3])
frase3= "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
#print(frase3[ : : -1])
#print(frase3.upper())
#print(frase3[1: :2].upper())
#print(frase3.split("a"))
#lista =frase3.split("e" +"e")
#print(lista)
#print(type(lista))
a= "Aprender"
b="Python"
c="Es"
d="Genial"
e = "-".join([a,b,c,d]) #va a unir todos los elementos en una lista separando con un espacio o el caracter que se le indique
print(e)
print(frase3.find("Es"))
lista_palabras = ["La","legibilidad","cuenta."]
#unir=(" ".join([lista_palabras]))
#print(unir)
#print(type(e))
frase4= "Si la implementación es dificil de explicar, puede que sea una mala idea."
print(frase4.replace("dificil","facil"))
print(frase4.replace("mala","buena"))