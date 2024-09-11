import os
from funciones import *


def menu():
    a = None
    b = None
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        
        opcion = int(input("Su opcion: "))
        
        if opcion == 1:
            print("Ingreso Primer Operando")
            a = ingresar_primer_operando()
        elif opcion == 2:
            print("Ingreso Segundo Operando")
            b = ingresar_segundo_operando()
        elif opcion == 3:
            if a == None or b == None:
                print('debe ingresar todos los operadores para ingresar.')
            else:
                print("Calculo todas las operaciones")
                calculo = True
                suma = sumar_operandos(a,b)
                resta = restar_operandos(a,b)
                division = calcular_division(a,b)
                multiplicacion = calcular_multiplicacion(a,b)
                potencia = calcular_potencia(a,b)
                resto = calcular_resto(a,b)
                factorial_a = calcular_factorial_a(a)
                factorial_b = calcular_factorial_b(b)

        elif opcion == 4:
            if calculo == False:
                print('hay que hacer los calculos antes de informarlos.')
            else:
                print("Informo todos los resultados")
                print(f'Suma: {suma}\nResta: {resta}\nDivisión: {division}\nMultiplicación: {multiplicacion}\nPotencia: {potencia}\nResto: {resto}\nFactorial A: {factorial_a}\nFactorial B: {factorial_b}\n')
                
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")
        input('Presione Enter Para Continuar.')
        os.system('cls')
    
    
menu()
