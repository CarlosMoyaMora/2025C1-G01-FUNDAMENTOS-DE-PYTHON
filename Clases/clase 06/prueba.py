
pregunta = True #al ser una condicion que no requiere un valor, le asignamos true.
articulo_1 = float(input('Porfavor, ingrese el precio de el primer atriculo:'))
pregunta = str(input('Desea ingresar otro articulo?:')) # pregunta que nos dira si entramos en el bucle o no
while (pregunta == 'si' .lower()): # condicion que se debe cumplir para que entremos o salgamos de el bucle
    precio_2 = float(input('Ingrese el nuevo producto:'))
    nuevo_precio = articulo_1 + precio_2
    articulo_1 = nuevo_precio
    pregunta = str(input('Desea ingresar otro articulo?:'))    

        
print(f'el precio final es: {articulo_1}')    
 # Finaliza el bucle.
