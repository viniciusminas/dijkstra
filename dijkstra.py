import heapq

def djikstra(ori, dest, grafo):
    fila = [(0, ori, [])]
    vistos = set()
    menor= {ori:0}

    while fila:
        (custo, vertice, caminho) = heapq.heappop(fila)

        if vertice in vistos:
            continue

        caminho = caminho + [vertice]
        vistos.add(vertice)

        if vertice == dest:
            return(custo, caminho)

        if vertice not in grafo:
            continue

        for prox_vertice, distancia in grafo[vertice].items():
            if prox_vertice in vistos:
                continue
            custo_previo = menor.get(prox_vertice, None)
            #A variavel custo_prévio, armazena o custo que se tinha para chegar na cidade até então
            prox_custo = custo + distancia
            if custo_previo is None or prox_custo < custo_previo:
                menor[prox_vertice] = prox_custo
                heapq.heappush(fila, (prox_custo, prox_vertice, caminho))

cidades = {
    'Rio do Sul': {'Ituporanga': 75, 'Petrolândia': 90, 'Atalanta': 18, 'Laurentino': 30, 'Agronômica': 66,
                   'Ibirama': 157.5},
    'Ituporanga': {'Rio do Sul': 75, 'Aurora': 26.4, 'Presidente Nereu': 90, 'Imbuia': 99, 'Atalanta': 17},
    'Ibirama': {'Imbuia': 178.2, 'Presidente Getúlio': 30, 'Rio do Sul': 157.5},
    'Petrolândia': {'Rio do Sul': 90, 'Atalanta': 18, 'Chapadao do Lageado': 110, 'Imbuia': 90},
    'Agronômica': {'Rio do Sul': 66, 'Laurentino': 24, 'Trombudo Central': 84, 'Atalanta': 12},
    'Atalanta': {'Rio do Sul': 18, 'Ituporanga': 17, 'Agronômica': 12, 'Petrolândia': 18},
    'Imbuia': {'Petrolândia': 90, 'Chapadao do Lageado': 66, 'Ibirama': 178.2, 'Ituporanga': 99},
    'Chapadao do Lageado': {'Petrolândia': 110, 'Imbuia': 66, 'Presidente Nereu': 132},
    'Aurora': {'Agronômica': 22, 'Ituporanga': 26.4},
    'Presidente Nereu': {'Chapadao do Lageado': 132, 'Ituporanga': 90},
    'Laurentino': {'Agronômica': 24, 'Dona Emma': 75, 'Rio do Sul': 30},
    'Trombudo Central': {'Agronômica': 84},
    'Presidente Getúlio': {'Ibirama': 30, 'José Boiteux': 99},
    'José Boiteux': {'Presidente Getúlio': 99},
    'Dona Emma': {'Laurentino': 75}
}

while True:
    origem = input('Origem: ')
    destino = input('Destino: ')

    try:
        custo_final, caminho_final = djikstra(origem, destino, cidades)

        if custo_final < float("inf"):
            print('O menor caminho entre a cidade {} e a cidade {} é: {}'.format(origem, destino, '-->'.join(caminho_final)))
            print('Custo do caminho: {}'.format(custo_final))
        else:
            print('Não há nenhum caminho entre {} e {}'.format(origem, destino))
    except:
        print('Ocorreu um erro inesperado!')

    print('--------------------------------------------------------------------------------------------------')

    ctrl = input('Deseja continuar verificando rotas?[S/n]')

    if ctrl != 'S' and ctrl != 's':
        break


