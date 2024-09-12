import os
from funciones import *


def menu():
    a = None
    b = None
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        
        opcion = int(input("Su opcion: "))
        
        if opcion == 1:
            a = ingresar_operando('ingrese primer operando: ')
        elif opcion == 2:
            b = ingresar_operando('ingrese segundo operando: ')
        elif opcion == 3:
            if a == None or b == None:
                print('debe ingresar todos los operadores para ingresar.')
            else:
                calculo = True
                suma = sumar_operandos(a,b)
                resta = restar_operandos(a,b)
                division = calcular_division(a,b)
                multiplicacion = calcular_multiplicacion(a,b)
                potencia = calcular_potencia(a,b)
                resto = calcular_resto(a,b)
                factorial_a = calcular_factorial(a)
                factorial_b = calcular_factorial(b)

        elif opcion == 4:
            if calculo == False:
                print('hay que hacer los calculos antes de informarlos.')
            else:
                print(f'El resultado de {a} + {b} es: {suma}\nEl resultado de {a} - {b} es: {resta}\nEl resultado de {a} / {b} es: {division}\nEl resultado de {a} * {b} es: {multiplicacion}\nEl resultado de {a} * {b} es: {potencia}\nEl resultado de {a} % {b} es: {resto}\nEl factorial de A es: {factorial_a} y El factorial de B es: {factorial_b}\n')
                
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")
        input('Presione Enter Para Continuar.')
        os.system('cls')
    
    
menu()
