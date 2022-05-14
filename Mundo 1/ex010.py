# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1.00 = R$3.27 

cotação = 3.27
reais = float(input("Quantos reais você tem? R$"))

print(f"Com R${reais} você pode comprar {int(reais // cotação)} dólar(es)")
