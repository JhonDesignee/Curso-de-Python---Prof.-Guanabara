# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

lista_retas = list()

for n in range(3):
  lista_retas.append(float(input(f"Digite o tamanho da {n + 1}° reta: ")))

r1, r2, r3 = lista_retas

if (abs(r2 - r3) < r1 < r2 + r3 and
  abs(r1 - r3) < r2 < r1 + r3 and
  abs(r1 - r2) < r3 < r1 + r2):
  print("Esses valores formam um triângulo")
else:
  print("Esses valores não formam um triângulo")
