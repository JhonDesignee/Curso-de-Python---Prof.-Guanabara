# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice

alunos = list()

for n in range(4):
  alunos.append(input(f"Digite o nome do {n + 1}° aluno: "))

escolhido = choice(alunos)

print(f"Aluno(a) escolhido(a): {escolhido}")

