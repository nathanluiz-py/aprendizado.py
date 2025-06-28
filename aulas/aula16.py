# if \ elif \ else
# se \ se nao se \ se naoo
# teste 1 com numeros

sistema = input('Digite seu sistema: ')
entrada = input ('digite sua idade ? ')
cov = int(entrada)

if cov <= 18:
    print(f'Bem vindo(a) {sistema} novo')

elif cov > 18 < 30:
    print(f'Bem vindo(a) {sistema} Jovem')

elif cov > 30 < 50:
    print(f'Bem vindo {sistema},Aduldo')

else :
    print(f'Bem vindo {sistema}, Velho')

print('Rodou')

# teste 2 com str

nome = input('Digite seu nome : ')
sistema = input('Você gostaria de "entrar" ou "sair" do sistema?  ')

if sistema == 'entrar':
    print(f'Bem vindo {nome}')

elif sistema == 'sair':
    print(f'Ate a proxima {nome}')

else :
    print(f'Opção invalida {nome} tente novamente')

print('Rodou')

