"""
Exercício
Exiba os índices da lista
0 nathan
1 luiz
2 aquino
"""
lista = ['nathan', 'luiz', 'aquino']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))