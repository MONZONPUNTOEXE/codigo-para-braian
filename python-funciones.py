# funciones con parametros


def suma(x, y):
    resultado = x + y

    return resultado


numero = int(input("Ingre un numero 1: "))
numero2 = int(input("Ingre un numero 2: "))


numero4 = 4
numero3 = 6

resultado_1 = suma(numero, numero2)
resultado_2 = suma(numero4, numero3)


print(resultado_1)
print(resultado_2)

# guardar_resultado_return = suma()
# print(guardar_resultado_return)


if resultado_2 == 10:
    print("El resultado es igual a 10")
else:
    print("No es igual a 10")


def validar():
    opcion = int(input("Ingrese un numero que no sea 10: "))
    if opcion == 10:
        return validar()
    else:
        print(f"El codigo ingesado: {opcion}")


validacion = validar()

# Importate: Guardar el resultado de la funcion que tiene "return" en una variable si se quiere printear o
# Si se quiere utilizar el resultado de esa funcion en otra operacion
