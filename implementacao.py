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
    for i in range(tam-1):
        itemAtual = vetor[i]
        while(True):
            posicao = i
            for item in vetor[i+1:]:
                if(item < itemAtual):
                    posicao += 1
            
            # Caso o valor já esteja na posição correta, parte para a próxima iteração
            if(posicao == i):
                vetor[i] = itemAtual
                break
            
            while(posicao < tam and vetor[posicao] == itemAtual):
                posicao += 1

            itemAtual, vetor[posicao] = vetor[posicao], itemAtual


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

iteracoes = 30
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
            for it in range(iteracoes):
                vetorOrdenar = vetor[:]

                inicio = time.perf_counter()
                funcao(vetorOrdenar, tam)
                fim = time.perf_counter()

                tempo = fim - inicio
                print(f"[{it+1}ª Iteração] Ordenado por {(funcao.__name__).upper()} em {tempo:.6f} segundos")
                # print(f"Saída: {vetorOrdenar}")