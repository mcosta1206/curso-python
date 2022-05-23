preço = float(input('Qual o preço de produto? R$'))
novo = preço(preço * 5 / 100)
print('O produto custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))
