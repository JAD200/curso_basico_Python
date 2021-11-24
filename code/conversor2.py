# -*- coding: latin-1 -*-
# Se utilizan """ para escribir un string largo
menu = """
💰💰Bienvenido al conversor de monedas💰💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion """

opcion = input(menu)

if opcion == 1:
    # Bloque de codigo
    pesos = input('Cuantos pesos colombianos tenes?: ')
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    pesos = str(pesos)
    print('Tienes ' + pesos + ' pesos colombianos que equivalen a $' + dolares + ' dolares')
elif opcion == 2:
    pesos = input('Cuantos pesos argentinos tenes?: ')
    pesos = float(pesos)
    valor_dolar = 100
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    pesos = str(pesos)
    print('Tienes ' + pesos + ' pesos argentinos que equivalen a $' + dolares + ' dolares')
elif opcion == 3:
    pesos = input('Cuantos pesos mexicanos tenes?: ')
    pesos = float(pesos)
    valor_dolar = 26
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    pesos = str(pesos)
    print('Tienes ' + pesos + ' pesos mexicanos que equivalen a $' + dolares + ' dolares')
else:
    print('* * * * ERROR * * * *')
    print('Ingresa una opcion correcta por favor')
