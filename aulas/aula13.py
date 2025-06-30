#Fstring
#:.2f (numero de casas decimais)

nome ='Marcio'
altura = 1.73
peso = 80
imc = peso / (altura * altura )
linha =f'O {nome} tem {altura:.2f} M de altura e pesa {peso} KG ,logo seu indeice de masa corporal e de {imc :.2f} kg'


print(linha)
