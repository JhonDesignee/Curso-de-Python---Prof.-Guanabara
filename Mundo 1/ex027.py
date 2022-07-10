# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. Ex: Ana Maria de Souza; primeiro = Ana; último = Souza

nome = input("Digite seu nome: ").strip()

print(f"Primeiro nome: {nome.split()[0]}")
print(f"Último nome: {nome.split()[-1]}")
