# Cantidad de pesos argentinos
pesos = input('Cuantos pesos tenes?: ')
pesos = float(pesos)
# Algoritmo para convertir pesos a dolares
valor_dolar = 100
dolares = pesos / valor_dolar
# Redondear decimales
dolares = round(dolares, 2)
# Tranformar resultados a strings o cadenas de texto para imprimir
dolares = str(dolares)
pesos = str(pesos)
print('Tienes ' + pesos + ' pesos argentinos que equivalen a $' + dolares + ' dolares')

print('==================================================')

# Cantidad de dolares
dolar = input('Cuantos dolares tenes?: ')
dolar = float(dolar)
# Algoritmo para convertir dolares a pesos
valor_pesos = 100
pesitos = dolar * valor_pesos
# Redondear decimales
pesitos = round(pesitos, 2)
# Tranformar resultados a strings o cadenas de texto para imprimir
pesitos = str(pesitos)
dolar = str(dolar)
print('Tienes $' + dolar + ' dolares que equivalen a ' + pesitos + ' pesos argentinos')