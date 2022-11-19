import folium


def generate_map(data):
    map = folium.Map(location=[42.9831, 47.504745], zoom_start = 8, tiles = "Stamen Terrain")

    for complaint in data:
        folium.Marker(location=[complaint['latitude'], complaint['longitude']], icon=folium.Icon(color = 'green')).add_to(map)

    map.save("static/map.html")