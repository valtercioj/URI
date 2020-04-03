cod1,qtd1,val1 = map(str,input().split())

cod1 = int(cod1)
qtd1= int(qtd1)
val1 = float(val1)
tot1 = qtd1 * val1
cod2,qtd2,val2 = map(str,input().split())

cod2 = int(cod2)
qtd2= int(qtd2)
val2 = float(val2)
tot2 = qtd2 * val2
valor = tot1 + tot2

print('VALOR A PAGAR: R$ {:.2f}'.format(valor))
