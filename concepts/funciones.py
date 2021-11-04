# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('Estoy aprendiendo a usar funciones en python!')

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def conversacion(opcion):
	print('Hola')
	print('Como estas?')
	opcion = str(opcion)
	print('Elegiste la opcion ' + opcion )
	print('Adios')

opcion = input('Elige una opcion (1, 2, 3): ')
if opcion == 1:
	conversacion(1)
elif opcion == 2:
	conversacion(2)
elif opcion == 3:
	conversacion(3)
else:
	print('* * * * ERROR * * * *')
	print('Elige la opcion correcta')