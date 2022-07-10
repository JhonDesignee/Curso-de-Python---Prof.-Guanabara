# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou iMPAR

número = int(input("Digite um número: "))

if número % 2 == 0:
  print(f"O número {número} é par")
else:
  print(f"O número {número} é ímpar")
