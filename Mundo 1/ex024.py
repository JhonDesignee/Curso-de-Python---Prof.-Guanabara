# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade_nome = input("Digite o nome da cidade: ").strip()
cidade_primeiro_nome = cidade_nome.split()[0].lower()

print(f"Começa com 'santo': {'santo' == cidade_primeiro_nome}")
