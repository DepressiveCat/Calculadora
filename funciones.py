def ingresar_primer_operando():
    a = input('ingrese primer operando: ')
    a = int(a)
    return a

def ingresar_segundo_operando():
    b = input('ingrese segundo operando: ')
    b = int(b)
    return b

def sumar_operandos(a,b):
    suma = a + b
    return suma

def restar_operandos(a,b):
    resta = a - b
    return resta

def calcular_division(a,b):
    if a == 0 or b == 0:
        return 'no se puede dividir por cero'
    division = a / b
    return division

def calcular_multiplicacion(a,b):
    multiplicacion = a * b
    return multiplicacion

def calcular_potencia(a,b):
    potencia = a ** b
    return potencia

def calcular_resto(a,b):
    resto = a % b
    return resto

def calcular_factorial_a(a):
    if a == 0:
        factorial_a = 1
    else: 
        factorial_a = a * calcular_factorial_a(a-1)    
    return factorial_a

def calcular_factorial_b(b):
    if b == 0:
        factorial_b = 1
    else: 
        factorial_b = b * calcular_factorial_b(b-1)
    return factorial_b 

