# Operadores in(entre) e not in(nao entre)
# string sao iteraveis
# 0 1 2 3 4 5
# | | | | | |
# n a t h a n
# | | | | | |
#-6-5-4-3-2-1
# nome = 'nathan'
# print (nome[0])=n
# print ('a' in nome)=true

nome = input('Digite seu nome: ')
buscar = input(f'qual letra voce gostaria de buscar no nome {nome} ? ')

if buscar in nome: #buscar por algo que tenha tendro da variavel nome
    print(f'a letra {buscar} esta presente no nome {nome}')

else:
    print(f'O nome {nome} nao tem a letra {buscar}')
