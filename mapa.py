import folium
from folium import plugins

stops_map = folium.Map(location=[-22.9440, -43.3419], zoom_start=12)
marker_cluster = folium.Marker(location=[-22.9440, -43.3419]).add_to(stops_map)
stops_map.save('minha_casa.html')
stops_map
