salário = float(input('Qual o salário do funcionario? R$'))
novo = salário + (salário * 15 / 100)
print('O funcionario que recebia R${:.2f}, com 15% de aumento, passa a receber R${}'.format(salário, novo))
