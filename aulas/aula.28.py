nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')


if nome and idade :
    print(f'Seu nome e:{nome}')
    print(f'Seu nome invertido e: {nome[::-1]}')
    print(f'O nome {nome} contem espaco ? {' ' in nome}')
    print(f'O nome {nome} tem : {len (nome)} letras')
    print(f'A primeira letra do seu nome e: {nome[0]}')
    print(f'A ultima letra do seu nome e: {nome[-1]}')
    

else:
    print('campos nao foram preenchidos')

