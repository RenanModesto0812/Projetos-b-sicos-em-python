print("1 - Residência (R$0,60)\n2 - Comércio (R$0,48)\n3 - Indústria (R$1,29)")
tipos = int(input("Digite o tipo de cliente: "))
consumo = float(input("Digite o consumo em kWh: "))

if tipos == 1:
    tarifa = 0.60
elif tipos == 2:
    tarifa = 0.48
elif tipos == 3:
    tarifa = 1.29
else:
    tarifa = 0
    print("Tipo de cliente inválido!")

valor = consumo * tarifa 
print(f"Valor da conta de luz: R${valor:.2f}") 
