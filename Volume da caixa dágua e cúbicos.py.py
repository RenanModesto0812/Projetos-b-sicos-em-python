import math

raio = float(input("Digite o raio da caixa d'água (m): "))
altura = float(input("Digite a altura da caixa d'água (m): "))

volume = math.pi * (raio ** 2) * altura

print(f"O volume da caixa d'água é: {volume:.2f} metros cúbicos")
