#ENTRADAS
print('porfavor ingrese un numero para mostrar su tabla del uno al 10')
numero_usuario = int(input())
multiplicacion = 5
#PROCESO
while(numero_usuario):
   if multiplicacion < 0 and multiplicacion <= 10:
            operacion = numero_usuario * multiplicacion
            print(f'{numero_usuario} x {multiplicacion} = {operacion}')