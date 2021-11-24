def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')

def palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    palabra_invertida = palabra[::-1]
    print(palabra_invertida)
    if palabra == palabra_invertida:
        return True
    else:
        return False

if __name__ == '__main__':
    run()