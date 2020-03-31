a,b = map(float,input().split())
c = ((b * 100) / a) - 100.00
print('{:.2f}%'.format(c))