# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira. Ex.: Digite um número: 6.127 O número 6.127 tem a parte Inteira 6

número = float(input("Digite um número real: ")) 

print(f"Parte inteira do número {número}: {int(número)}")
