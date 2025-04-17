# archivo para almacenar
# Funciones que quiero reutilizar a Futuro
import csv, os, pandas as pd


def ingresar_ventas(lista_ventas):
    while True:
        try:
            curso = input('Ingrese el nombre del curso: ').upper()
            cantidad = int(input('Ingrese la cantidad de cursos vendidos: '))
            fecha = input('Ingrese la fecha de la venta (AAAA-MM-DD): ')
            precio= float(input('Ingrese el precio del curso: '))
            cliente = input('Ingrese el nombre del cliente: ').upper()
        except ValueError:
            print('El valor no es correcto, por favor intentelo nuevamente!')
            continue
        
        venta = {
            'curso' : curso,
            'cantidad' : cantidad,
            'precio' : precio,
            'fecha' : fecha,
            'cliente' : cliente
        }    
        
        lista_ventas.append(venta)
            
            #Ingresar las ventas
        continuar= input('Desea ingresar otra venta s/n : ').lower()
            
        if continuar == 's':    
            print('\n--- Ingresando otra venta ---')       
        elif continuar == 'n':    
            print('\n--- Ingresando otra venta ---')
            break   
        else:
            print('Opcion no valida')
    print(venta)            

def guardar_ventas(ventas):
    if not ventas:
        print('No hay ventas que guardar en el CSV')
    else:
        if os.path.exists('ventas.csv'):
            #si el archivo existe agrego Append  'A'
            with open('ventas.csv','a',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['curso','cantidad','precio','fecha','cliente'])
                guardar.writerows(ventas)        
        else: #Si no existe abro en modo escritura 'W'
            with open('ventas.csv','w',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['curso','cantidad','precio','fecha','cliente'])
                guardar.writeheader()
                guardar.writerows(ventas)
                
        #Limpio las ventas en memoria y muestro el guardado exitoso                
        ventas = []
        print('Datos guardados exitosamente!') 


def analisis_ventas():
    df = pd.read_csv('ventas.csv')
    print('\n------------- RESUMEN DE VENTAS-------------')
                            