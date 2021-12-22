# Projecto 1
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1.- Crear un menu que nos muestre las opciones.
# 2.- Crear un input que uses con numeros decimales y cada numero se use para un tipo de calculo.
import time
active = False
while not(active):
    print("  *********  calculadora  *********")
    print("1) Suma\n2) Resta\n3) Multiplicacion\n4) Division\n5) Salir\n  **********************************")

    choose = int(input("Introduzca el numero: "))
    if choose == 1:
        #suma
        sum1=int(input("Introducca primer numero para la suma: "))
        sum2=int(input("Introducca primer segunda para la suma: "))
        resultado = sum1 + sum2
        print(sum1,"+",sum2,"= ",resultado)
        time.sleep(2)
    elif choose == 2:
        #resta
        resta1=int(input("Introduzca el primer numero de la resta: "))
        resta2=int(input("Introduzca el segundo numero de la resta: "))
        resultado = resta1 - resta2
        print(resta1,"+",resta2,"= ",resultado)
        time.sleep(2)
    elif choose == 3:
        #multipilicacion
        multi1=int(input("Introduzca el primer numero de la multiplicaciones: "))
        multi2=int(input("Introduzca el segundo numero de la multiplicaciones: "))
        resultado=multi1*multi2
        print(multi1,"+",multi2,"= ",resultado)
        time.sleep(2)
    elif choose == 4:
        #division
        dividendo=int(input("Introduzca el dividendo: "))
        divisor=int(input("Introduzca el divisor: "))
        resultado=dividendo/divisor
        print(dividendo,"+",divisor,"= ",resultado)
        time.sleep(2)
    elif choose == 5:
        print("Saliendo de la calculadora.")
        for item in range(2):
            print("*")
            time.sleep(1)
        break


# Proyecto 2 (Funciones)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Funciones
 
def calculadora(a,b):
    return suma(a, b), resta(a, b), multiplicacion(a, b), dividir(a, b)


def suma(suma1,suma2):
    return suma1 + suma2

def resta(minuendo, sustraendo):
    return minuendo - sustraendo

def multiplicacion(multi1, multi2):
    return multi1 * multi2

def dividir(divisor, dividendo):
    return divisor / dividendo
onOf= False
while not(onOf):
    print("  ******************  calculadora  ******************")
    print("1) Suma\n2) Resta\n3) Multiplicacion\n4) Division\n5) Salir\n  ****************** (ft. Funciones) ****************")
    choose = int(input("Introduzca la operacion: "))
    if choose == 1:
        resultado = suma(int(input('Introduzca el primer valor: ')), int(input('Introduzca el segundo valor: ')))
        print("El resultado es:",resultado)
        time.sleep(2)
    elif choose == 2:
        resultado = resta(int(input("Introduzca el minuendo valor: ")),int(input("Introduzca el sustraendo valor: ")))
        print("El resultado es:", resultado)
        time.sleep(2)
    elif choose == 3:
        resultado = multiplicacion(int(input("Introduzca el minuendo valor: ")),int(input("Introduzca el sustraendo valor: ")))
        print("El resultado es:", resultado)
        time.sleep(2)
    elif choose == 4:
        resultado = dividir(int(input("Introduzca el minuendo valor: ")),int(input("Introduzca el sustraendo valor: ")))
        print("El resultado es:", resultado)
        time.sleep(2)
    elif choose == 5:
        print('saliendo de la calculadora')
        for item in range(2):
            print('*')
        break