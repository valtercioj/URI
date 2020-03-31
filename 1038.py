x,y = map(int,input().split())
if x == 1:
    cq = y*4.00
    print('Total: R$ {:.2f}'.format(cq))
elif x == 2:
    xSalada = y*4.50
    print('Total: R$ {:.2f}'.format(xSalada))
elif x == 3:
    xBacon = y*5.00
    print('Total: R$ {:.2f}'.format(xBacon))
elif x == 4:
    Torrada = y*2.00
    print('Total: R$ {:.2f}'.format(Torrada))
elif x == 5:
    refrigerante = y*1.50
    print('Total: R$ {:.2f}'.format(refrigerante))