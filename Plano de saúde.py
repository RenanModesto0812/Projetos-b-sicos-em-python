nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

if idade <= 10:
    valor = 130
elif idade <= 29:
    valor = 240
elif idade <= 45:
    valor = 280
elif idade <= 59:
    valor = 320
elif idade <= 65:
    valor = 390
else:
    valor = 1360

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Valor do plano de saúde: R${valor:.2f}")
