# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = input("Digite seu nome: ").strip()
nome = nome.lower()

print(f"O nome tem 'Silva': {'silva' in nome}")
