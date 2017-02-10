import folium
import pandas

vlcns=pandas.read_csv('Volcanoes-USA.txt')

def color(elev):
	minimo=int(min(vlcns['ELEV']))
	paso=int(min(vlcns['ELEV'])/4)
	if elev in range(minimo, minimo+paso):
		color='green'
	elif elev in range(minimo+paso, minimo+paso*2):
		color='yellow'
	elif elev in range(minimo+paso*2, minimo+paso*3):
		color='orange'
	else:
		color='red'

	return color

map=folium.Map(location=[vlcns['LAT'].mean(), vlcns['LON'].mean()], zoom_start=4, tiles='Stamen Terrain')

fg=folium.FeatureGroup(name='Volcanes')

for lat, lon, name, elev in zip(vlcns['LAT'],vlcns['LON'], vlcns['NAME'], vlcns['ELEV']):
	fg.add_child(folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color(elev))))

map.add_child(fg)

map.add_child(folium.GeoJson(data=open('world_pop.json'),
name='Poblacion',
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] <= 10000000 else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(folium.LayerControl())

map.save(outfile="test.html")
