# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu. 

from random import randint

número_sorteado = randint(0, 5)
número_escolhido = int(input("Escolha um número entre 0 e 5: "))

if número_escolhido == número_sorteado:
  print("Parabéns! Você acertou")
else:
  print("Que pena! Você errou")
print(f"O computador escolheu o número {número_sorteado}")
