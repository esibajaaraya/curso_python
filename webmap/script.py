import folium
import pandas

map=folium.Map(location=[45.372, -121.697], zoom_start=4, tiles='Stamen Terrain')
vlcns=pandas.read_csv('Volcanoes-USA.txt')

for lat, lon, name in zip(vlcns['LAT'],vlcns['LON'], vlcns['NAME']):
	map.simple_marker(location=[lat, lon], popup=name,marker_color='red')


map.create_map(path="test.html")
