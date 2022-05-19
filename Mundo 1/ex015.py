# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R50,15 por Km rodado

km = float(input("Quilômetros percorridos: "))
dias = int(input("Dias alugado: "))
total = km * 0.15 + dias * 60

print(f"Total a pagar: R${total:.2f}")
