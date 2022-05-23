frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra aparece {} vezes na frase. '.format(frase.count('A')))
print('A primeira letra apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra apareceu na posição {}'.format(frase.rfind('A')+1))
