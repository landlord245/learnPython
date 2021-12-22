# En esta fase aprenderemos como usar los funciones
# def significa que vamos a usar funcion

# Ejercicio 1
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# En este caso no le daremos un para metro de entrada ni nada
# La propia funcion tendra el codigo que necesitamos
def Saludar():
    print("Hola  mundo")

# Esta funcion nos devuelve un print, por lo que solo lo llamaremos sin usar ni print ni nada.
Saludar()

# Ejercicio 2
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ahora crearemos una funcion que nos permite saber si un numero es mayor que 0
def MayorQue(param):
    if param > 0:
        print(param,"es  mayor que cero")
    else:
        print(param,"no es mayor que cero")

# Aqui sus diferentes salidas
MayorQue(0)
MayorQue(1)
MayorQue(-2)

numero = int(input("Introduzca un numero: "))
MayorQue(numero)

# Ejercicio 3
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ahora vamos a crear una funcion que nos permite sumar
def sumar1(a, b):
    return a + b

numero1 = int(input("Introduzca un numero: "))
numero2 = int(input("Introduzca un numero: "))

# en este caso vemos que le podemos indicar los inputs
#para solicitar una salida, lo tenemos que pasar a una variable
resultado = sumar1(numero1, numero2)
print(resultado)


# Ejercicio 4
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ahora vamos a realizar una funcin mas compleja, consistira en que si le pasamos un valor, la funcion podra pasar dos tipos de resultados
# presta atencion ...
def SumaResta(a, b):
    return a + b, a - b

numero1 = int(input("Introduzca un numero: "))
numero2 = int(input("Introduzca un numero: "))

# Ahora pediremos que nos devuelva una suma y una resta
suma, resta = SumaResta(numero1, numero2) # La posicion de la variable es muy importante.

print("Esto es una resta:",resta)
print("Esto es una suma:",suma)


# Ejercicio 5
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Sumar2(*valor):
    resultado = 0
    for item in valor:
        resultado = resultado+ item
    return resultado

# Vale esta funcion esta rara pero es facil de entender, bien lo que hace es que le pasamos un valor (que se almacena en el parametro "valor") digamos un 12
# resultado = Sumar2(12)
# Cuando ejecutamos, el bucle for hace la cantidad de iteraciones que le hemos pedido (12 en nuestro caso)
# pero si lo concatenamos con mas numeros (12, 12) lo que hace es ejecutar 12 veces y sigue con el siguiente, que en este caso es 12 pero estavez lo suma, ya que lo va guardando en la misma variable
resultado = Sumar2(12, 12)
print(resultado)

# Ejercicio 6
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#En este ejercico usaremos una funcion para hacer otra funcion y si queremos podemos ir usando mas, esto dependera de la necesidad

def sumaResta(a,b):
    return suma(a,b), resta(a,b)

def suma(suma1,suma2):
    return suma1 + suma2

def resta(minuendo, sustraendo):
    return minuendo, sustraendo