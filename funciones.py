def ingresar_operando(mensaje):
    a = input(mensaje)
    a = int(a)
    return a

def sumar_operandos(a,b):
    suma = a + b
    return suma

def restar_operandos(a,b):
    resta = a - b
    return resta

def calcular_division(a,b):
    if a == 0 or b == 0:
        return 'No es posible dividir por cero'
    division = a / b
    return division

def calcular_multiplicacion(a,b):
    multiplicacion = a * b
    return multiplicacion

def calcular_potencia(a,b):
    potencia = a ** b
    return potencia

def calcular_resto(a,b):
    if a == 0 or b == 0:
        return 'No es posible dividir por cero'
    resto = a % b
    return resto

def calcular_factorial(numero):
    if numero == 0:
        factorial = 1
    else: 
        factorial = numero * calcular_factorial(numero-1)    
    return factorial
