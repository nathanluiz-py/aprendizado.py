# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
# and ele checa se as duas opcoes sao verdadeiras,caso uma nao seja ele pula 

entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Digite uma senha :') 

senha_permitida = '1234'

if entrada == 'E' or entrada =='e' and senha_digitada == senha_permitida :
    print('vc entrou')
else :
    print('Acesso negado')


senha = input('digite uma senha: ') or 'favor digitar uma senha'
print(senha) 

