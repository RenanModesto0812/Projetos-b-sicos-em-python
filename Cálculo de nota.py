Seu_Nome = (input("Digite Seu nome: "))
nota1 = float(input("Digite a segunda nota: "))
nota2 = float(input("Digite a terceira nota: "))
nota3 = float(input("Digite a segunda nota: "))
nota4 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"Aluno: {Seu_Nome}")

if media > 7:
    print(f"Aprovado! Disk estuda. Média: {media:.2f}")
elif media < 7:
    print(f"Reprovado! se lascou ótario. Média: {media:.2f}")
else:
    print(f"Prova final! Média: {media:.2f}")
