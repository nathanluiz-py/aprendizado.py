#exercicio para ver qual valor e maior   
val_1 = input('Digite o primeiro valor: ')
val_2 = input('Digite o segundo valor: ')

#val1 = int(val_1)
#val2 = int(val_2)

if val_1 > val_2 :#poderia por menor ou igual e retirar o elif
    print(f'o valor 1 e: {val_1} ele e maior que que o valor 2: {val_2}')

elif val_2 > val_1 :
    print(f'o valor 2 e: {val_2} ele e maior que o valor 1: {val_1}')

else :
    print (f'{val_1} é {val_2} são iguais')
