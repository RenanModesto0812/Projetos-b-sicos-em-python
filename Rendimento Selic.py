deposito = float(input("Digite o valor do depósito: "))
taxa_selic = float(input("Digite a taxa de juros (%): "))

rendimento = deposito * (taxa_selic / 100)
total = deposito + rendimento

print(f"Rendimento: R${rendimento:.2f}")
print(f"Total após rendimento: R${total:.2f}")
