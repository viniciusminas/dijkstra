from flask import Flask, render_template, request
import heapq

app = Flask(__name__)


def djikstra(ori, dest, grafo):
    fila = [(0, ori, [])]
    vistos = set()
    menor = {ori: 0}

    while fila:
        (custo, vertice, caminho) = heapq.heappop(fila)

        if vertice in vistos:
            continue

        caminho = caminho + [vertice]
        vistos.add(vertice)

        if vertice == dest:
            return (custo, caminho)

        if vertice not in grafo:
            continue

        for prox_vertice, distancia in grafo[vertice].items():
            if prox_vertice in vistos:
                continue
            custo_previo = menor.get(prox_vertice, None)
            prox_custo = custo + distancia
            if custo_previo is None or prox_custo < custo_previo:
                menor[prox_vertice] = prox_custo
                heapq.heappush(fila, (prox_custo, prox_vertice, caminho))

    return (float('inf'), [])


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

cidades_lat_lon = {
    'Rio do Sul': {'lat': -27.2156, 'lon': -49.643},
    'Ituporanga': {'lat': -27.4133, 'lon': -49.5967},
    'Ibirama': {'lat': -27.0544, 'lon': -49.5192},
    'Petrolândia': {'lat': -27.5347, 'lon': -49.6964},
    'Agronômica': {'lat': -27.2667, 'lon': -49.7078},
    'Atalanta': {'lat': -27.4211, 'lon': -49.7789},
    'Imbuia': {'lat': -27.4903, 'lon': -49.4217},
    'Chapadao do Lageado': {'lat': -27.5903, 'lon': -49.5517},
    'Aurora': {'lat': -27.3097, 'lon': -49.6297},
    'Presidente Nereu': {'lat': -27.2764, 'lon': -49.3875},
    'Laurentino': {'lat': -27.2175, 'lon': -49.7331},
    'Trombudo Central': {'lat': -27.2975, 'lon': -49.7894},
    'Presidente Getúlio': {'lat': -27.0478, 'lon': -49.6256},
    'José Boiteux': {'lat': -26.9567, 'lon': -49.6283},
    'Dona Emma': {'lat': -26.9814, 'lon': -49.7222}
}


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        origem = request.form['origem']
        destino = request.form['destino']

        try:
            custo_final, caminho_final = djikstra(origem, destino, cidades)

            if custo_final < float("inf"):
                caminho_str = ' --> '.join(caminho_final)
                return render_template('index.html',  caminho=caminho_str, custo=custo_final)
            else:
                return render_template('index.html', caminho="Nenhum caminho encontrado", custo="Indisponível")
        except:
            return render_template('index.html', caminho="Erro ao calcular a rota", custo="Indisponível")

    return render_template('index.html', caminho=None)


if __name__ == '__main__':
    app.run(debug=True)

