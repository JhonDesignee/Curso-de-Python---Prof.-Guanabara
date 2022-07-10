# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R50.45 para viagens mais longas

distância = float(input("Distância da viagem: Km"))

if distância <= 200:
  print("Preço por Km: R$0,50")
  print(f"Valor da passagem: R${distância * 0.50:.2f}")
else:
  print("Preço por Km: R$0,45")
  print(f"Valor da passagem: R${distância * 0.45:.2f}")
