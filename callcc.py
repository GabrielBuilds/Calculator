numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))

print('Escolha a operação:\n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão')

operacao = input('Digite o numero da operação desejada: ')

if operacao == '1':
    resultado = numero1 + numero2
elif operacao == '2':
    resultado = numero1 - numero2
elif operacao == '3':
    resultado = numero1 * numero2
elif operacao == '4':
    resultado = numero1 / numero2
print('O resultado da operação é de {:.2f}' .format(resultado))