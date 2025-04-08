import random, time

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

def gerarConjuntos(tamanhos: list[int]):
    listas = []
    for tam in tamanhos :
        dicionario = {
            "crescente": [i for i in range(tam)],
            "decrescente": [i for i in range(tam-1, -1, -1)],
            "aleatorio": [random.randint(0, tam-1) for i in range(tam)],
        }
        listas.append(dicionario)

    return listas

def linha(char: str = "=", tam: int = 70):
    print(char * tam)


random.seed(2025)

tamanhos = [10_000, 50_000, 100_000]

listas = gerarConjuntos(tamanhos)

for item, tam in zip(listas, tamanhos):
    linha()
    print(f"CONJUNTO DE {tam} ITENS")
    for nome, vetor in item.items():
        linha(char="-", tam=30)
        print(f"{nome.capitalize()}", end="")
        # print(f": {vetor}")
        print()
        for funcao in [heapSort, cycleSort]:
            vetorOrdenar = vetor[:]

            inicio = time.perf_counter()
            funcao(vetorOrdenar, tam)
            fim = time.perf_counter()

            tempo = fim - inicio
            print(f"Ordenado por {(funcao.__name__).upper()} em {tempo:.6f} segundos")
            # print(f"Saída: {vetorOrdenar}")