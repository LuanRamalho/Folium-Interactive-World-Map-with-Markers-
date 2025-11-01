import folium

map_world = folium.Map(location=[20,0], zoom_start=2)

cities = {"New York":[40.7128, -74.0060],
          "Tokyo":[35.6895, 139.6917],
          "Delhi":[28.6139, 77.2090],
          "Rio de Janeiro":[-22.9068, -43.1729], 
          "Paris":[48.8566, 2.3522],            
          "Lagos":[6.5244, 3.3792]}           

for city, coords in cities.items():
    # Use folium.Marker para adicionar um marcador
    folium.Marker(
        location=coords, 
        popup=city
    ).add_to(map_world)

# Salva o mapa interativo no arquivo HTML
map_world.save("mapa_mundial_atualizado.html")
print("Arquivo 'mapa_mundial_atualizado.html' criado com sucesso com as novas cidades!")