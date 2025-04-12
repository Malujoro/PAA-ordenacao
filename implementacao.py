import random, time

def heapify(vetor: list[int], tam: int, raiz: int):
    maior = raiz
    esquerdo = 2 * raiz + 1
    direito = 2 * raiz + 2

    if(esquerdo < tam and vetor[esquerdo] > vetor[maior]):
        maior = esquerdo

    if(direito < tam and vetor[direito] > vetor[maior]):
        maior = direito

    if(maior != raiz):
        vetor[raiz], vetor[maior] = vetor[maior], vetor[raiz]

        heapify(vetor, tam, maior)

def heapSort(vetor: list[int], tam: int):
    primeiroPai = tam // 2 - 1

    # Constrói o max heap (organiza a árvore)
    for i in range(primeiroPai, -1, -1):
        heapify(vetor, tam, i)

    # Efetua as trocas e reorganiza a árvore
    for i in range(tam-1, 0, -1):
        vetor[i], vetor[0] = vetor[0], vetor[i]
        heapify(vetor, i, 0)

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

tamanhos = [10]
# tamanhos = [10_000, 50_000, 100_000]

listas = gerarConjuntos(tamanhos)
listas[0]["aleatorio"] = [8, 1, 10, 7, 2, 8, 0, 5, 6, 9]

for item, tam in zip(listas, tamanhos):
    linha()
    print(f"CONJUNTO DE {tam} ITENS")
    for nome, vetor in item.items():
        linha(char="-", tam=30)
        print(f"{nome.capitalize()}", end="")
        print(f": {vetor}")
        print()
        for funcao in [heapSort]:
        # for funcao in [heapSort, cycleSort]:
            vetorOrdenar = vetor[:]

            inicio = time.perf_counter()
            funcao(vetorOrdenar, tam)
            fim = time.perf_counter()

            tempo = fim - inicio
            print(f"Ordenado por {(funcao.__name__).upper()} em {tempo:.6f} segundos")
            print(f"Saída: {vetorOrdenar}")