precio_producto = float(input('Porfavor ingrese el priecio de el producto:'))
nuevo_prod =input('Si desea ingresar un nuevo producto escriba si, de los contrario escriba no')
nuevo_prod != 'si'
while(nuevo_prod):
   nuevo_precio = float(input('Ingrese el precio de el nuevo articulo'))
   suma_productos = precio_producto + nuevo_precio
   precio_producto = suma_productos
   repetir = input('Si desea ingresar un nuevo producto escriba si, de los contrario escriba no')
   if repetir != 'si':
      print(F'Gracias por su compra, Total a pagar: {precio_producto}')     