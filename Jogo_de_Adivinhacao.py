import random
import time
import matplotlib.pyplot as plt

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    tempo_inicial = time.time()
    
    while True:
        palpite = int(input("Adivinhe o número entre 1 e 100: "))
        tentativas += 1
        
        if palpite < numero_secreto:
            print("Muito baixo!")
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
            break
    
    tempo_final = time.time()
    tempo_gasto = tempo_final - tempo_inicial
    return tentativas, tempo_gasto

# Coletando dados
dados = []
for _ in range(5):  # Jogar 5 vezes para coletar dados
    tentativas, tempo = jogo_adivinhacao()
    dados.append((tentativas, tempo))

# Analisando dados
tentativas_totais = [d[0] for d in dados]
tempos_totais = [d[1] for d in dados]

# Visualizando dados
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(range(1, 6), tentativas_totais)
plt.title('Tentativas por Jogo')
plt.xlabel('Jogo')
plt.ylabel('Número de Tentativas')

plt.subplot(1, 2, 2)
plt.bar(range(1, 6), tempos_totais)
plt.title('Tempo por Jogo (segundos)')
plt.xlabel('Jogo')
plt.ylabel('Tempo Gasto')

plt.tight_layout()
plt.show()