# archivo para almacenar
# Funciones que quiero reutilizar a Futuro

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