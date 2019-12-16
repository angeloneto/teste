n1 = int(input('insira o primeiro valor: '))
n2 = int(input('insira o segundo valor: '))

soma = n1+n2
subtrair = n1-n2
multiplicar = n1*n2
dividir = n1/n2
op = input('insira a operação desejada: ')
if op == "+":
	print('o valor da soma é: ',soma)
elif op == "-":
	print('o valor da subtração é: ',subtrair)
elif op == "*":
	print('o valor da multiplicação é: ',multiplicar)
elif op == "/":
	print('o valor da divisão é: ',dividir)