# Arreglos

arreglos = ["a", "p", "g", "u", "r"]
compra = [
    "Compras de a",
    "Compras de p",
    "Compras de g",
    "Compras de u",
    "Compras de r",
]

# Buscar un dato del arreglo:
# cat indica el indice, por convension usamos la letra "i" de "Index"
for cat in range(len(arreglos)):
    # Iteramos la cantidad de elementos que tenga el arreglo
    if "g" == arreglos[cat]:  # En la vuelta que encuentre "g" ingresa al bloque
        print(cat)
        # imprime "g"
        print(arreglos[cat])  # arreglos[2]
        print(compra[cat])  # compra[2]

# Otra forma de Busqueda:
# cat toma la forma de los datos que tiene "arreglos"
for cat in arreglos:
    if cat == "g":
        print(cat)
        print("encontraste la G perro")
