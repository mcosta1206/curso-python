número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O numero {} é PAR'.format(número))
else:
    print('O número {} é IMPAR'.format(número))