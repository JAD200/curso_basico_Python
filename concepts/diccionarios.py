def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44_938_712,
        'Brazil': 210_147_125,
        'Colombia': 50_372_424
    }
#Solo imprime ese item
    # print(poblacion_paises['Argentina'])
#solo imprime las keys
    # for pais in poblacion_paises.keys():
    #     print(pais)
#Solo imprme los valores
    # for pais in poblacion_paises.values():
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes\n')

if __name__ == '__main__':
    run()