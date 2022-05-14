# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salário = float(input("Digite o salário: R$"))

print(f"Salário com 15% de aumento: R${salário + 15 / 100 * salário:.2f}")
