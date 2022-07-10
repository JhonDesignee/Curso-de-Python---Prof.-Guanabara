# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

lista_números = list()

for n in range(3):
  lista_números.append(float(input(f"Digite o {n + 1}° número: ")))

print(f"O maior número é: {max(lista_números)}")
print(f"O menor número é: {min(lista_números)}")
