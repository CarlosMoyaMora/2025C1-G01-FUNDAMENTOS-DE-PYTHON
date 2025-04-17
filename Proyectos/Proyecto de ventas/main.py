"""
Autor: Carlos Andrey Moya Mora
Fecha: 16/04/2025
Version: 0.1
Sistema de Gestion de ventas Que permita ingresar, almacenar y analizar datos
"""
import os

from modulo import ingresar_ventas, guardar_ventas


def limpiar_pantalla():# esta funcion limpia la terminal en ejecucion.
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    input('\n--- Presione enter para continuar ---')  
    


#Vamos a Crear un Menu para que el Usuario elija que hacer

def menu():
    while True:
        print('\n---- Menu Principal ----')
        print('1. Ingresar Ventas de cursos UMCA')
        print('2. Guardar datos en un archivo CSV')
        print('3. Analizar las ventas')
        print('4. Salir')
        opcion = input('Ingrese una opcion: ')
        
        if opcion == '1':
            limpiar_pantalla()
            print('\n---Ingreso de ventas de Cursos')
            ingresar_ventas(ventas)
            pausar()
            
        elif opcion == '2':
            limpiar_pantalla
            print('\n---Guardar Ventas en CSV')
            guardar_ventas(ventas)
            pausar()
        elif opcion == '3':
            print('\n--- Analisis de Ventas---')
            pausar()
        elif opcion == '4':
            print('\n--- Gracias por usar el sistema. Hasta pronto!')
            pausar()
            break #<- cierro el sistema determinado el ciclo while.
        
        else:
            print('Opcion no Valida. Intente nuevamente una opcion!')


                  

# Ejecucion del sistema solo si el archivo es el Main

if __name__ == '__main__':
    print('Bienvenido al sistema de Gestion de Ventas')
    
    ventas = []
    
    
    pausar()
    menu()

