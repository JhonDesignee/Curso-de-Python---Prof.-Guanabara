# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados. Ex: Digite um número: 1834; unidade: 4 dezena: 3 centena: 8 milhar: 1

número = input("Digite um número entre 0 e 9999: ").strip()
número = f"{número:0>4}"

print(f"Unidade: {número[3]}")
print(f"Dezena: {número[2]}")
print(f"Centena: {número[1]}")
print(f"Milhar: {número[0]}")
