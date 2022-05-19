# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

alunos = list()

for n in range(4):
  alunos.append(input(f"Digite o nome do {n + 1}° aluno: "))
shuffle(alunos)

apresentação_ordem = ", ".join(alunos)
apresentação_ordem = apresentação_ordem[::-1].replace(",", "e ", 1)[::-1]

print(f"Ordem de apresentação dos trabalhos: {apresentação_ordem}")
