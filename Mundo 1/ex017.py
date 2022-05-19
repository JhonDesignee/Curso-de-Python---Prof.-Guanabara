# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

cateto_oposto = float(input("Cateto oposto: "))
cateto_adjacente = float(input("Cateto adjacente: "))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5

print(f"A hipotenusa de {cateto_oposto:.2f} e {cateto_adjacente:.2f} é: {hipotenusa:.2f}")
