import folium
from folium import Icon
import json
import urllib.request

# ALTERE AQUI a cor de fundo da página em hexadecimal
COR_FUNDO_HEX = "#1a1a2e"
COR_PAISES = "#4a7c9e"
COR_BORDA_PAISES = "#ffffff"

def hex_para_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    if len(hex_color) != 6:
        raise ValueError("Cor hexadecimal inválida. Use o formato #RRGGBB")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Cria o mapa sem tiles
m = folium.Map(
    location=[20, 0],
    zoom_start=2,
    tiles=None,
    control_scale=True,
    min_zoom=1,
    max_zoom=6,
    no_wrap=True,
    prefer_canvas=True
)

# Fundo da página e do mapa
rgb = hex_para_rgb(COR_FUNDO_HEX)

# Adiciona fundo sólido por CSS
m.get_root().header.add_child(folium.Element(f"""
<style>
    body {{
        margin: 0;
        background-color: {COR_FUNDO_HEX};
    }}
    .leaflet-container {{
        background: {COR_FUNDO_HEX} !important;
    }}
    .leaflet-tile-pane {{
        display: none !important;
    }}
    .leaflet-control-zoom {{
        display: block;
    }}
</style>
"""))

# GeoJSON dos países
geojson_url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"

try:
    with urllib.request.urlopen(geojson_url) as response:
        geo_data = json.loads(response.read())

    folium.GeoJson(
        geo_data,
        style_function=lambda x: {
            "fillColor": COR_PAISES,
            "color": COR_BORDA_PAISES,
            "weight": 1,
            "fillOpacity": 0.7,
            "dashArray": "0"
        }
    ).add_to(m)

except Exception:
    print("Não foi possível carregar o GeoJSON dos países. O mapa continua sem divisões geográficas.")

# Cidades
cities = {
    "New York": [40.7128, -74.0060],
    "Tokyo": [35.6895, 139.6917],
    "Delhi": [28.6139, 77.2090],
    "Rio de Janeiro": [-22.9068, -43.1729],
    "Paris": [48.8566, 2.3522],
    "Lagos": [6.5244, 3.3792],
}

cores_marcadores = ["red", "blue", "green", "orange", "purple", "darkred"]
for i, (city, coords) in enumerate(cities.items()):
    folium.Marker(
        location=coords,
        popup=f"<b>{city}</b>",
        tooltip=city,
        icon=Icon(color=cores_marcadores[i], icon="info-sign", prefix="fa")
    ).add_to(m)

m.save("mapa_mundial.html")

print("Arquivo salvo: mapa_mundial.html")
print(f"Cor de fundo atual: {COR_FUNDO_HEX}")
print("Mapa sem tiles, com países visíveis e sem bloqueio de API.")
