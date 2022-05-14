# Desafio 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

valor = input("Digite algo: ")

print(f"Valor digitado: {valor}")
print(f"Tipo primitivo: {type(valor)}")
print(f"É numérico? {valor.isnumeric()}")
print(f"É alfabético? {valor.isalpha()}")
print(f"É alfanumérico? {valor.isalnum()}")
print(f"Está em caixa alta? {valor.isupper()}")
print(f"Está em caixa baixa? {valor.islower()}")
print(f"É um espaço? {valor.isspace()}")
