# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

valor = int(input("Digite um número: "))

for n in range(11):
  print(f"{valor} × {n} = {valor * n}")
