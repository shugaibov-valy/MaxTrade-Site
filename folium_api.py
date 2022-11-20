import folium
from geocoder import coords_to_address


icon_path = r"Znak.png"

def generate_map(default_address=None, default_location=None, complaints=None, marks=None):
    if default_location is None and default_address is None:
        map = folium.Map(location=[42.9831, 47.504745], zoom_start = 16, tiles = "Stamen Terrain")
        
        ### метки минстроя
        for mark in marks:
            danger_icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(50,50))
            folium.Marker(location=[mark['latitude'], mark['longitude']], 
                                icon=danger_icon,
                                popup=f"<p>{mark['streetName'].split('Россия, ')[1]}</p><a target='_blank' href='/mark/{mark['id']}'>подробнее...</a>").add_to(map)


        ### жалобы пользователей
        for complaint in complaints:
            street = complaint['streetName'].split("Россия, ")[1]
            folium.Marker(location=[complaint['latitude'], complaint['longitude']], 
                            icon=folium.Icon(color = 'green'),
                            popup=f"<strong>{complaint['title']}</strong><p>{street}</p><a target='_blank' href='/card/{complaint['id']}'>подробнее...</a>").add_to(map)

        map.save("static/map.html")
    else:
        default_location = [default_location[1], default_location[0]]
        map = folium.Map(location=default_location, zoom_start = 16, tiles = "Stamen Terrain")
    

        ### default метка при вводе адресе
        folium.Marker(location=[default_location[0], default_location[1]], 
                            icon=folium.Icon(color = 'red'),
                            popup=f"<p>{default_address.split('Россия, ')[1]}</p><a target='_blank' href='/mark/create_mark/latitude={default_location[0]}&longitude={default_location[1]}'>создать метку</a>").add_to(map)


        ### метки минстроя
        for mark in marks:
            danger_icon = folium.features.CustomIcon(icon_image=icon_path ,icon_size=(50,50))
            folium.Marker(location=[mark['latitude'], mark['longitude']], 
                                icon=danger_icon,
                                popup=f"<p>{mark['streetName'].split('Россия, ')[1]}</p><a target='_blank' href='/mark/{mark['id']}'>подробнее...</a>").add_to(map)




        ### жалобы пользователей
        for complaint in complaints:
            street = complaint['streetName'].split("Россия, ")[1]
            folium.Marker(location=[complaint['latitude'], complaint['longitude']], 
                            icon=folium.Icon(color = 'green'),
                            popup=f"<strong>{complaint['title']}</strong><p>{street}</p><a target='_blank' href='/card/{complaint['id']}'>подробнее...</a>").add_to(map)

        map.save("static/map.html")


