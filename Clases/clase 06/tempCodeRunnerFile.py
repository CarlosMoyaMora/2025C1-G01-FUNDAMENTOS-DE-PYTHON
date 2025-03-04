try:
    precio_producto = float(input('favor ingrece el precio de el primer producto'))    
    while (precio_producto):
        nuevo_prod = str(input('Si desea ingresar un nuevo producto escriba si, de los contrario escriba no'))
        if nuevo_prod != 'si' .lower:
            while (nuevo_prod):
                nuevo_precio = float(input('ingrese el precio'))
            break
    print('gracias por su compra')           
except ValueError:
    print('Error: por favor ingrese un valor numerico correcto.')