# Escreva um programa que pergunte o salário da um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250.00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

salário = float(input("Digite o salário: "))

if salário > 1250:
  print(f"Seu salário, com aumento de 10%, será de R${salário + 10 / 100 * salário:.2f}")
else:
  print(f"Seu salário, com aumento de 15%, será de R${salário + 15 / 100 * salário:.2f}")
