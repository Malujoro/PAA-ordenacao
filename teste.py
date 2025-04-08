import random

random.seed(2025)

tam = 10
crescente = [i for i in range(tam)]
decrescente = [i for i in range(tam-1, -1, -1)]
aleatorio = [random.randint(0, tam) for i in range(tam)]

print(f"Crescente: {crescente}")
print(f"Decrescente: {decrescente}")
print(f"Aleatório: {aleatorio}")

def heapSort(vetor: list[int], tam: int):
    for quantidade in range(tam-1, -1, -1):
        for filho in range(quantidade, 0, -1):
            pai = (filho - 1) // 2
            if(vetor[filho] > vetor[pai]):
                vetor[filho], vetor[pai] = vetor[pai], vetor[filho]

        vetor[quantidade], vetor[0] = vetor[0], vetor[quantidade]

def cycleSort(vetor: list[int], tam: int):
    for it in range(tam-1):
        aux = vetor[it]
        while(True):
            quantMenor = 0

            for item in vetor[it+1:]:
                if(item < aux):
                    quantMenor += 1
            
            if(quantMenor == 0):
                vetor[it] = aux
                break
            
            posicao = quantMenor + it
            while(vetor[posicao] == aux):
                posicao += 1

            aux, vetor[posicao] = vetor[posicao], aux


for funcao in [heapSort, cycleSort]:
    for vetor in [aleatorio[:], crescente[:], decrescente[:]]:
        print(vetor)
        funcao(vetor, tam)
        print(vetor)
        print()