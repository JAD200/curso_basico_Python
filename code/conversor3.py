# -*- coding: latin-1 -*-
def conversor(tipo_pesos, valor_dolar):
    pesos = input('Cuantos pesos ' + tipo_pesos + ' tienes?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    pesos = str(pesos)
    print('Tienes ' + pesos + ' pesos ' + tipo_pesos + ' que equivalen a $' + dolares + ' dolares')
# Se utilizan """ para escribir un string largo
menu = """
💰💰Bienvenido al conversor de monedas💰💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion por favor """

opcion = input(menu)

if opcion == 1:
    conversor('colombianos', 3875)
elif opcion == 2:
    conversor('argentinos', 100)
elif opcion == 3:
    conversor('mexicanos', 24)
else:
    print('* * * * ERROR * * * *')
    print('Ingresa una opcion correcta por favor')
