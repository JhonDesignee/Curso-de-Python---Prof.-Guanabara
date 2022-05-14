# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preço = float(input("Preço do produto: R$"))

print(f"Produto com 5% de desconto: R${preço - 5 / 100 * preço:.2f}")
