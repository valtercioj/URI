N = int(input())
valor = N
n100 = N // 100
N %= 100
n50 = N // 50
N %= 50
n20 = N // 20
N %= 20
n10 = N // 10
N %= 10
n5 = N // 5
N %= 5
n2 = N // 2
N %= 2
n1 = N
print(valor)
print("{} nota(s) de R$ 100,00".format(n100))
print("{} nota(s) de R$ 50,00".format(n50))
print("{} nota(s) de R$ 20,00".format(n20))
print("{} nota(s) de R$ 10,00".format(n10))
print("{} nota(s) de R$ 5,00".format(n5))
print("{} nota(s) de R$ 2,00".format(n2))
print("{} nota(s) de R$ 1,00".format(n1))