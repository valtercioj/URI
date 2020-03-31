valor = float(input())
reais = int(valor)
centavos = int((valor - reais) * 100)

n100 = reais // 100
reais = reais - (n100 * 100)
n50 = reais // 50
reais = reais - (n50 * 50)
n20 = reais // 20
reais = reais - (n20 * 20)
n10 = reais // 10
reais = reais - (n10 * 10)
n5 = reais // 5
reais = reais - (n5 * 5)
n2 = reais // 2
reais = reais - (n2 * 2)

m1 = 0
if reais:
    m1 = 1

m50 = centavos // 50
centavos = centavos - (m50 * 50)
m25 = centavos // 25
centavos = centavos - (m25 * 25)
m10 = centavos // 10
centavos = centavos - (m10 * 10)
m05 = centavos // 5
centavos = centavos - (m05 * 5)
m01 = centavos

print ("NOTAS:")
print (n100, "nota(s) de R$ 100.00")
print (n50, "nota(s) de R$ 50.00")
print (n20, "nota(s) de R$ 20.00")
print (n10, "nota(s) de R$ 10.00")
print (n5, "nota(s) de R$ 5.00")
print (n2, "nota(s) de R$ 2.00")
print ("MOEDAS:")
print (m1, "moeda(s) de R$ 1.00")
print (m50, "moeda(s) de R$ 0.50")
print (m25, "moeda(s) de R$ 0.25")
print (m10, "moeda(s) de R$ 0.10")
print (m05, "moeda(s) de R$ 0.05")
print (m01, "moeda(s) de R$ 0.01")