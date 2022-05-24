casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = float(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100 
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, ano), end='')
print(' A prestação será de {:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO! ')
else:
    print('Empréstimo NEGADO!')
    