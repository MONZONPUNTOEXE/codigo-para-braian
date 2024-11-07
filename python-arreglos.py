# Arreglos

arreglos = ["a", "p", "g", "u", "r"]
compra = ["3 perros", "2 mocos", "cositas", "mas perros", "una Speed"]

# Buscar un dato del arreglo:
for caca in range(len(arreglos)):
    if "g" == arreglos[caca]:
        print(caca)
        print(arreglos[caca])
        print(compra[caca])

# Otra forma de Busqueda:
# Caca toma la forma de los datos que tiene "arreglos"
for caca in arreglos:
    if caca == "g":
        print(caca)
        print("encontraste la G perro")
