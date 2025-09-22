salario_hora = float(input("Digite o valor do salário por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
inss= float(input("Digite o percentual de desconto do INSS (%): "))
salario_bruto = salario_hora * horas_trabalhadas
desconto = salario_bruto * (inss / 100)
salario_liquido = salario_bruto - desconto

print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"Desconto INSS: R${desconto:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")
