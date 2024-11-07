# funciones con parametros

# Los parametros cuando se CUANDO SE DEFINEN pueden tener cualquier nombre
# Lo mejor es colocarle un nombre descriptivo y
# que tenga que ver con el contexto

# Ejemplo:


def suma(x, y):
    resultado = x + y

    return resultado


# numeros que definie el usuario


numero = int(input("Ingre un numero 1: "))
numero2 = int(input("Ingre un numero 2: "))

# variables hard Codeados
numero4 = 4
numero3 = 6

# return nos devuelve el dato que tiene "resultado"
# Para que luego podemos usar ese dato para lo que necesitemos
# Para guardar el dato que nos devuelve return en este caso "resultado"
# Lo podemos guardar en una variable

resultado_1 = suma(numero, numero2)
resultado_2 = suma(numero4, numero3)

# printeamos
print(resultado_1)
print(resultado_2)


if resultado_2 == 10:
    print("El resultado es igual a 10")
else:
    print("No es igual a 10")

# Implementamos recursividad


def validar():
    opcion = int(input("Ingrese un numero que no sea 10: "))
    if opcion == 10:
        return validar()
    else:
        print(f"El codigo ingesado: {opcion}")


validacion = validar()

# Importate: Guardar el resultado de la funcion que tiene "return" en una variable
# si se quiere printear o
# si se quiere utilizar el resultado de esa funcion en otra operacion
