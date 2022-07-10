# Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez

frase = input("Digite qualquer frase: ").strip()
frase = frase.lower()

print(f"Quantidade de letras 'a': {frase.count('a')}")
print(f"Posição do primeiro 'a': {frase.find('a') + 1}")
print(f"Posição do último 'a': {frase.rfind('a') + 1}")
