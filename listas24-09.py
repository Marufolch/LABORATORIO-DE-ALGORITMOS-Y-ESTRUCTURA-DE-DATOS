mi_lista = ["perro", 22, 10.5, "manzana", False]
#print (mi_lista)

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
#print(medios_transporte)

frutas = [ "manzana","banana", "mango", "cereza","sandía"]
#print(frutas)
eliminado = frutas.pop(3)
#print(frutas)
print(eliminado)

mi_diccionario = {"curso":"Python TOTAL"
,
"clase":"Diccionarios"}

mi_diccionario["recursos"] = ["notas"
,
"ejercicios"]
#print(mi_diccionario.keys())
#print(mi_diccionario.values())
#print(mi_diccionario.items())
#print(mi_diccionario)
mi_dic = {"nombre" : "julia", "apellido":"Jurgens", "edad": 35,"ocupacion": "periodista"}
#print(mi_dic)
# Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
#print(mi_dict["puntos"]["points2"][1])
#print(mi_dict["valores_1"]["v1"])
mi_dic["nombre"]= "Karen"
mi_dic["edad"]= 36
mi_dic["ocupacion"]= "editora"
mi_dic["pais"]= "colombia"
#print(mi_dic)
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
#print(mi_tupla.count(2))
mi_tupla2 = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista= list(mi_tupla)
#print(mi_lista)
mi_tupla3 = (1, 2, 3, 4)
a,b,c,d = mi_tupla3
print(mi_tupla3)