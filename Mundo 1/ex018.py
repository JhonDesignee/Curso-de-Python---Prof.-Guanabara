# Faça um programa que leia um ângulo qualquer e mostre na tala o valor do seno, cosseno o e tangente desse ângulo

from math import radians, sin, cos, tan

ângulo = radians(float(input("Digite o ângulo: ")))

print(f"Seno: {sin(ângulo):.2f}")
print(f"Cosseno: {cos(ângulo):.2f}")
print(f"Tangente: {tan(ângulo):.2f}")
