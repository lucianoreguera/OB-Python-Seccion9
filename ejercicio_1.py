paises = input("Ingrese países separados por una coma(,): ")

lista_paises = paises.split(',')

print(lista_paises)

set_paises = set(lista_paises)

print(set_paises)

sorted_paises = sorted(set_paises)

print(sorted_paises)
