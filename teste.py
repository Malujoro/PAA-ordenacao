import random

random.seed(2025)

tam = 10
crescente = [i for i in range(tam)]
decrescente = [i for i in range(tam-1, -1, -1)]
aleatorio = [random.randint(0, tam) for i in range(tam)]
aleatorio2 = aleatorio[:]

print(f"Crescente: {crescente}")
print(f"Decrescente: {decrescente}")
print(f"Aleatório: {aleatorio} {aleatorio2}")

def heapSort(vetor: list[int], tam: int):
    quantidade = tam-1
    while(quantidade >= 0):
        for filho in range(quantidade, 0, -1):
            pai = (filho - 1) // 2
            if(vetor[filho] > vetor[pai]):
                vetor[filho], vetor[pai] = vetor[pai], vetor[filho]

        vetor[quantidade], vetor[0] = vetor[0], vetor[quantidade]
        quantidade -= 1


for vetor in [aleatorio, crescente, decrescente]:
    print(vetor)
    heapSort(vetor, tam)
    print(vetor)
    print()

# Fórmula para encontrar posição do filho:
# I * 2 + 1 (esquerda)
# I * 2 + 2 (direita)

# Fórmula para encontrar posição do pai:
# (Posição - 1) // 2

#  0, 1, 2,  3, 4, 5, 6, 7, 8, 9
# [8, 1, 10, 7, 2, 8, 0, 5, 6, 9]
# 0 - 1 e 2
# 1 - 3 e 4
# 2 - 5 e 6
# 3 - 7 e 8
# 4 - 9 e 10