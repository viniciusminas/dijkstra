# Exemplo de grafo com custos
graph = {
    'Rio do Sul': {'Ituporanga': 75, 'Petrolândia': 90, 'Atalanta': 18, 'Laurentino': 30, 'Agronômica': 66, 'Ibirama': 157.5},
    'Ituporanga': {'Rio do Sul': 75, 'Aurora': 26.4, 'Nereu': 90, 'Imbuia': 99, 'Atalanta': 17},
    'Ibirama': {'Rio do Sul': 157.5, 'Imbuia': 178.2, 'Getúlio': 30,  'Presidente Getulio': 30},
    'Petrolândia': {'Rio do Sul': 90, 'Atalanta': 18, 'Chapadão': 110, 'Imbuia': 90},
    'Agronômica': {'Rio do Sul': 66, 'Laurentino': 24, 'Trombudo Central': 84, 'Atalanta': 12},
    'Atalanta': {'Rio do Sul': 18, 'Ituporanga': 17, 'Agronômica': 12, 'Petrolandia': 18},
    'Imbuia': {'Petrolândia': 90, 'Chapadão': 66, 'Ibirama': 178.2, 'Ituporanga': 99},
    'Chapadão': {'Petrolândia': 110, 'Imbuia': 66, 'Presidente Nereu': 132},
    'Aurora': {'Agronomica': 22, 'Ituporanga': 26.4}
    'Presidente Nereu': {'Chapadão do Lageado': 132, 'Ituporanga': 90},
    'Laurentino': {'Agronomica': 24, 'Dona Emma': 75, 'Rio do Sul': 30},
    'Trombudo Central': {'Agronômica': 84},
    'Presidente Getúlio': {'Ibirama': 30, 'José Boiteux': 99},
    'José Boiteux': {'Presidente Getúlio': 99},
    'Dona Emma': {'Laurentino': 75}
}