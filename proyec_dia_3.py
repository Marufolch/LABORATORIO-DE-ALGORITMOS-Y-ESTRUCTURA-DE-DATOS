print("ingrese un breve texto o una frase que tenga al menos 5 palabras")
texto =input("")
print("ahora, igrese 3 letras a su eleccion:")
l1 = input("letra 1: ")
l2 = input("letra 2: ")
l3 = input("letra 3: ")
texto2 = texto.upper()

letras1= texto.count(l1)
letras2= texto.count(l2)
letras3 = texto.count(l3)
print(f' en la frase que escribio hay {letras1} letras "{l1.upper()}", {letras2} letras "{l2.upper()}", y {letras3} letras "{l3.upper()}"')
palabra = texto.split()

print(f' La frase que escribio tiene {len(palabra)} palabras')
print(f'El texto comienza con la la letra "{texto[0]}" y termina con la letra "{texto[-1]}" ')
palabra.reverse()
" ".join(palabra)
print(f' Si quisieramos ver la frase con el el orden invertido, seria algo asi: {" ".join(palabra)}')
py2= "python" in texto
#esto es otra opcion para obtener el resultado, decidi no borrarlo
#if py2 == False:
    #print("La palabra 'python' no esta en este texto")
#else:
    #print("El texto contiene la palabra python")
diccio = {True: "la palabra python esta en el texto", False: "la palabra python no esta en el texto"}
print(diccio[py2])
print("bueno, eso es todo. has terminado.")