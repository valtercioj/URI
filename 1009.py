NOME = str(input())
SALARIO = float(input())
VENDAS = float(input())

TOTAL = SALARIO + (VENDAS*0.15)
print('TOTAL = R$ {:.2f}'.format(TOTAL))