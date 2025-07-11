"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
append : adiciona item ao final
insert : adiciona um item ao um dice escolhido
pop : remove do final ou indice escolhido
del : apaga um indice
clear : limpa a lista
extend : estende a lista 
+ : concatenar a lista
,
Create Read Update Delete (CRUD)

"""
# string = 'ABCDE'  # 5 caracteres (len)
# # print(bool([]))  # falsy
# # print(lista, type(lista))

# #        0    1            2         3   4
# lista = [123, True, 'Luiz Otávio',  1.2, []]
# lista[-3] = 'Nathan' #alterar o valor pelo indice
# print(lista) 
# print(lista[2], type(lista[2]))


lista =[1,2,3,4,5,6]
del lista[0] #ira retirar o numero 1 da lista
lista.append(7) #adicionar item ao final da lista
lista.insert(0, 0)
lista.pop(0) #remove o ultimo CASO SEJA VAZIO, CASO PASSE O INDICE ELE REMOVERA O INDICE INDICADO
lista.clear()
print(lista)


lista_a = [1]
lista_b = [2]

# ou
lista_a.extend(lista_b)
print(lista_a)


lista_x = [3,4]
lista_y = lista_x.copy #copiando os dados de uma lista para outra

print(lista_y)