a = int(input())
anos = a // 365
meses = (a % 365) // 30
dias = (a % 365) % 30
print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))