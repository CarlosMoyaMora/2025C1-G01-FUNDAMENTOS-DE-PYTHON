
precio_producto = float(input('Porfavor ingrese el priecio de el producto:'))

while(precio_producto):
   nuevo_prod =input('Si desea ingresar un nuevo producto escriba si, de los contrario escriba no')
   if nuevo_prod != 'si':
         nuevo_precio = float(input('Ingrese el precio de el nuevo articulo'))
         suma_productos = precio_producto + nuevo_precio
         precio_producto = suma_productos
      
               

