a = 'A'   #posicao0
b = 'B'   #posicao1
c = 1.1   #posicao2
string = 'a={n1} ,b={n1}, c={n1}, {n1},{n1},{n1}' #indices,ele busca pela posicao que a variavel esta 
# formato = string.format(a,b,c) #aqui e o argumento,ele puxa da variavel os valores mais tamb pode ser declarado a mao 
formato = string.format(n1=a,n2=b,n3=c) #parametro nomeados,todos parametros devem ser nomeados caso seja usado assim


print(formato)