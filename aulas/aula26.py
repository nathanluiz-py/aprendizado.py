"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #largura fixa para preencher a esquerda
print(f'{variavel:<10}.') #largura fixa para preencher a direita
print(f'{variavel:^10}.')#ao centro
print(f'{1000.4873648123746:0=+10,.1f}')#formatar numero
print(f'O hexadecimal de 1500 é {1500:020X}') #variavel e depois coloca o numero de casas desejadas,sempre comecar com zero
print(f'{variavel!r}')


#caso queira preencher com algo so colocar um caractere antes dossinais ><^