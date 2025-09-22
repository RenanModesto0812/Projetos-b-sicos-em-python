tempo = float(input("Digite o tempo gasto na viagem (h): ")) 
velocidade = float(input("Digite a velocidade média (km/h): "))

distancia = tempo * velocidade
litros = distancia / 41

print(f"Distância percorrida: {distancia:.2f} km")
print(f"Combustível necessário: {litros:.2f} litros")
