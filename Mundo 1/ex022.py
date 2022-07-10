# Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas, o nome com todas minúsculas, quantas letras ao todo (sem considerar espaços) e quantas letras tem o primeiro nome

nome = input("Digite seu nome completo: ").strip()


print(f"Maiusculo: {nome.upper()}")
print(f"Minúsculo: {nome.lower()}")
print(f"Letras: {len(nome.replace(' ', ''))}")
print(f"Letras no primeiro nome: {len(nome.split()[0])}")
