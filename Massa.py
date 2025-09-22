massa = float(input("Digite a massa inicial (g): "))
tempo = 0  
massa_inicial = massa

while massa >= 0.5: 
    massa /= 2
    tempo += 50
    
horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 60

print(f"Massa inicial: {massa_inicial} g")
print(f"Massa final: {massa:.2f} g")
print(f"Tempo: {horas}h {minutos}m {segundos}s")
