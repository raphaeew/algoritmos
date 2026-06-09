import random
import time


# FUNÇÃO PARA VERIFICAR SE A LISTA FICOU ORDENADA

def verificar_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


# 1 - SELECTION SORT

def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        menor = i

        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]

    return lista


# 2 - BUBBLE SORT

def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


# 3 - INSERTION SORT

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j = j - 1

        lista[j + 1] = chave

    return lista


# 4 - MERGE SORT

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    resultado = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i = i + 1
        else:
            resultado.append(direita[j])
            j = j + 1

    resultado = resultado + esquerda[i:]
    resultado = resultado + direita[j:]

    return resultado


# 5 - QUICK SORT

def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista) // 2]

    menores = []
    iguais = []
    maiores = []

    for valor in lista:
        if valor < pivo:
            menores.append(valor)
        elif valor == pivo:
            iguais.append(valor)
        else:
            maiores.append(valor)

    return quick_sort(menores) + iguais + quick_sort(maiores)


# 6 - HEAP SORT

def ajustar_heap(lista, tamanho, raiz):
    maior = raiz
    esquerda = 2 * raiz + 1
    direita = 2 * raiz + 2

    if esquerda < tamanho and lista[esquerda] > lista[maior]:
        maior = esquerda

    if direita < tamanho and lista[direita] > lista[maior]:
        maior = direita

    if maior != raiz:
        lista[raiz], lista[maior] = lista[maior], lista[raiz]
        ajustar_heap(lista, tamanho, maior)


def heap_sort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        ajustar_heap(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        ajustar_heap(lista, i, 0)

    return lista


# 7 - COUNTING SORT

def counting_sort(lista):
    if len(lista) == 0:
        return lista

    menor = min(lista)
    maior = max(lista)

    contagem = [0] * (maior - menor + 1)

    for valor in lista:
        contagem[valor - menor] = contagem[valor - menor] + 1

    resultado = []

    for i in range(len(contagem)):
        quantidade = contagem[i]
        valor_original = i + menor

        for j in range(quantidade):
            resultado.append(valor_original)

    return resultado


# 8 - RADIX SORT

def counting_sort_por_digito(lista, casa):
    tamanho = len(lista)
    resultado = [0] * tamanho
    contagem = [0] * 10

    for valor in lista:
        digito = (valor // casa) % 10
        contagem[digito] = contagem[digito] + 1

    for i in range(1, 10):
        contagem[i] = contagem[i] + contagem[i - 1]

    i = tamanho - 1
    while i >= 0:
        valor = lista[i]
        digito = (valor // casa) % 10
        resultado[contagem[digito] - 1] = valor
        contagem[digito] = contagem[digito] - 1
        i = i - 1

    for i in range(tamanho):
        lista[i] = resultado[i]


def radix_sort(lista):
    if len(lista) == 0:
        return lista

    maior = max(lista)
    casa = 1

    while maior // casa > 0:
        counting_sort_por_digito(lista, casa)
        casa = casa * 10

    return lista


# 9 - BUCKET SORT

def bucket_sort(lista):
    if len(lista) == 0:
        return lista

    menor = min(lista)
    maior = max(lista)
    quantidade_baldes = 10

    baldes = []

    for i in range(quantidade_baldes):
        baldes.append([])

    for valor in lista:
        if maior == menor:
            indice = 0
        else:
            indice = int((valor - menor) / (maior - menor) * (quantidade_baldes - 1))

        baldes[indice].append(valor)

    resultado = []

    for balde in baldes:
        insertion_sort(balde)
        resultado = resultado + balde

    return resultado


# FUNÇÃO PARA TESTAR CADA ALGORITMO

def testar_algoritmo(nome, funcao, lista_teste):
    copia = lista_teste.copy()

    inicio = time.time()
    resultado = funcao(copia)
    fim = time.time()

    tempo = fim - inicio
    ordenada = verificar_ordenada(resultado)

    print("--------------------------------------------")
    print("Algoritmo:", nome)
    print("Quantidade de elementos:", len(lista_teste))
    print("Tempo gasto:", round(tempo, 4), "segundos")
    print("Lista ordenada corretamente:", ordenada)


# RESUMO PARA APRESENTAÇÃO


def mostrar_vantagens_desvantagens():
    print("\nRESUMO DOS ALGORITMOS")

    print("\nSelection Sort")
    print("Vantagem: simples de entender e implementar.")
    print("Desvantagem: lento para listas grandes, pois faz muitas comparações.")

    print("\nBubble Sort")
    print("Vantagem: fácil de visualizar, pois compara elementos vizinhos.")
    print("Desvantagem: muito ineficiente para grandes quantidades de dados.")

    print("\nInsertion Sort")
    print("Vantagem: bom para listas pequenas ou quase ordenadas.")
    print("Desvantagem: fica lento quando a lista é grande e muito desorganizada.")

    print("\nMerge Sort")
    print("Vantagem: eficiente para listas grandes e tem bom desempenho constante.")
    print("Desvantagem: usa mais memória, pois divide e cria novas listas.")

    print("\nQuick Sort")
    print("Vantagem: geralmente é muito rápido na prática.")
    print("Desvantagem: pode piorar dependendo da escolha do pivô.")

    print("\nHeap Sort")
    print("Vantagem: tem bom desempenho e não depende de lista auxiliar grande.")
    print("Desvantagem: é mais difícil de entender por usar a ideia de heap.")

    print("\nCounting Sort")
    print("Vantagem: muito rápido quando os números estão em um intervalo conhecido.")
    print("Desvantagem: não é ideal quando o intervalo dos valores é muito grande.")

    print("\nRadix Sort")
    print("Vantagem: eficiente para ordenar números inteiros com várias casas decimais.")
    print("Desvantagem: funciona melhor em números inteiros não negativos.")

    print("\nBucket Sort")
    print("Vantagem: pode ser rápido quando os dados estão bem distribuídos.")
    print("Desvantagem: perde eficiência se muitos valores caírem no mesmo balde.")


# PROGRAMA PRINCIPAL

print("TRABALHO DE ALGORITMOS DE ORDENAÇÃO")
print("Criando lista com 100.000 elementos aleatórios...")

lista_grande = []

for i in range(100000):
    numero = random.randint(0, 999999)
    lista_grande.append(numero)

lista_pequena = lista_grande[:2000]

print("Lista grande criada com", len(lista_grande), "elementos.")
print("Lista menor criada com", len(lista_pequena), "elementos para os algoritmos mais lentos.")

print("\nOBSERVAÇÃO IMPORTANTE")
print("Selection Sort, Bubble Sort e Insertion Sort são simples, mas ficam muito lentos com 100.000 elementos.")
print("Por isso, eles serão demonstrados com 2.000 elementos, para evitar travamento e mostrar a diferença de desempenho.")
print("Os algoritmos mais eficientes serão testados com a lista completa de 100.000 elementos.")

testar_algoritmo("Selection Sort", selection_sort, lista_pequena)
testar_algoritmo("Bubble Sort", bubble_sort, lista_pequena)
testar_algoritmo("Insertion Sort", insertion_sort, lista_pequena)

testar_algoritmo("Merge Sort", merge_sort, lista_grande)
testar_algoritmo("Quick Sort", quick_sort, lista_grande)
testar_algoritmo("Heap Sort", heap_sort, lista_grande)
testar_algoritmo("Counting Sort", counting_sort, lista_grande)
testar_algoritmo("Radix Sort", radix_sort, lista_grande)
testar_algoritmo("Bucket Sort", bucket_sort, lista_grande)

mostrar_vantagens_desvantagens()

print("\nFim dos testes.")