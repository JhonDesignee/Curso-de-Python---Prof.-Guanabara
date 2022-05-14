# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua Área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input("Largura da parede (em metros): "))
altura = float(input("Altura da parede (em metros): "))
área = largura * altura

print(f"Área da parede: {área}m²")
print(f"Quantidade de tinta necessária: {área / 2}l")
