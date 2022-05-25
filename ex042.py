peso = float(input('Quak é seu peso? (kg) '))
altura = float(input('Qual é sua açtura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉN, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE! ')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
  