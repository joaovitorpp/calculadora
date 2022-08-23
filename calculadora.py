with open('resultado.txt', 'w') as arquivo:
 x=float(input("coloque um numero para entrar na operção: "))

 y=float(input("coloque o segundo numero para a operação: "))

 z=input('''
escolha qual operação deseja fazer:
+ para adição
- para subtração
* para multiplicação
/ para divisão
% para resto
''')

#adição
 if z == '+':
  print('{} + {} = '.format(x, y))
  print(x+y)
  p=(x+y)
      
  
#subtração
 if z == '-':
  print('{} - {} ='.format(x, y))
  print(x-y)
  p=(x-y)
  
#multiplicação
 if z == '*':
  print('{} * {} ='.format(x, y))
  print(x*y)
  p=(x*y)
  
 

#divisão
 if z == '/':
  if y==0:
   print("erro, divisão por 0 não existe")
   p=("erro, divisão por 0 não existe")
  else:
   print('{} / {} ='.format(x, y))
   print(x/y)
   p=(x/y)
   
    
   
#resto
 if z == '%':
  print('{} % {} ='.format(x, y))
  print(x%y)
  p=(x%y)

 

 print(p, file=arquivo)