"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# num = input('Digite um número inteiro: ')

# try:
#     num_int = int(num)
#     if num_int % 2 == 0:
#         print('Par')
#     elif num_int % 2 != 0:
#         print('Ímpar')
# except:
#     print('Não é um número inteiro.')

    



# """
# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. 
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
# """

# hr = float(input('digite a hora:'))

# bd = hr >= 0 and hr <=11
# bt = hr > 11 and hr <= 17


# if bd:
#     print('Bom dia')
# elif bt:
#     print('boa tarde')
# else:
#     print('boa noite')


# #Com try
# hr = input('digite a hora: ')

# try:
#     hrx = int(hr)
#     if hrx >= 0 and hrx <=11:
#         print(f'Agora sao {hrx}hrs da manha, Bom dia')

#     elif hrx > 11 and hrx <=17:
#         print(f'Agora sao {hrx}hrs da tarde, Boa tarde') 

#     elif hrx > 17 and hrx <= 23:
#         print(f'Agora sao {hrx}hrs da noite, Bom noite')

#     else:
#         print('hora fora do intervalo entre 0 e 23')
# except:
#     print('informe uma hora inteira')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')
nome_num = len(nome)


if nome_num >1 and nome_num <= 4 :
        print(f'seu nome e {nome},ele e muito curto')
elif nome_num > 4 and nome_num <= 6 :
        print(f'seu nome e {nome},ele e normal') 
elif nome_num > 6:
        print(f'seu nome e {nome},ele e grande')
else:
        print('vc n digitou nada ')

