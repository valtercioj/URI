n1,n2,n3,n4 = map(float,input().split())
media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10
print('Media: {:.1f}'.format(media))
if media >= 7.0:
    print('Aluno aprovado.')
if media < 5.0:
    print('Aluno reprovado.')
if 5.0 <= media <= 6.9:
    print('Aluno em exame.')
    y = float(input())
    print('Nota do exame: {}'.format(y))
    m2 = (y + media) / 2
    if m2 >=5.0:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(m2))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(m2))
