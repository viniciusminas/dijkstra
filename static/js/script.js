var map = L.map('map').setView([-27.2156, -49.643], 12);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var coordenadas = {
    'Rio do Sul': {'lat': -27.2156, 'lon': -49.643},
    'Ituporanga': {'lat': -27.4133, 'lon': -49.5967},
    'Ibirama': {'lat': -27.0544, 'lon': -49.5192},
    'Petrolândia': {'lat': -27.5347, 'lon': -49.6964},
    'Agronômica': {'lat': -27.2667, 'lon': -49.7078},
    'Atalanta': {'lat': -27.4211, 'lon': -49.7789},
    'Imbuia': {'lat': -27.4903, 'lon': -49.4217},
    'Chapadão do Lageado': {'lat': -27.5903, 'lon': -49.5517},
    'Aurora': {'lat': -27.3097, 'lon': -49.6297},
    'Presidente Nereu': {'lat': -27.2764, 'lon': -49.3875},
    'Laurentino': {'lat': -27.2175, 'lon': -49.7331},
    'Trombudo Central': {'lat': -27.2975, 'lon': -49.7894},
    'Presidente Getúlio': {'lat': -27.0478, 'lon': -49.6256},
    'José Boiteux': {'lat': -26.9567, 'lon': -49.6283},
    'Dona Emma': {'lat': -26.9814, 'lon': -49.7222}
};

i = 0;
function addPopUps(caminho_pop){
    caminho_pop.forEach(element => {
        i += 5;
        let lat = -27.0544 + i;
        let lon = -49.5192 + i;
        L.marker([lat, lon]).addTo(map)
            .bindPopUp(element)
            .addPopUp();
    });
}

addPopUps(caminho);
