# San Fran latitude and longitude
lat = 37.77
long = -122.42

# geojson file
world_geo = r'SanFran.json' 

# set linear spacing from min to max
threshold_scale = np.linspace(df_sf['Count'].min(),
df_sf['Count'].max(),
6, dtype = int)

# convert numpy array to a list
threshold_scale = threshold_scale.tolist()

# check last value of the list is greater than max
threshold_scale[-1] = threshold_scale[-1] + 1 

# generate map and choropleth
world_map = folium.Map(location = [lat, long], zoom_start = 12)
world_map.choropleth(
geo_data = world_geo,
data = df_sf,
columns = ['Neighborhood', 'Count'],
key_on = 'feature.properties.DISTRICT',
threshold_scale = threshold_scale,
fill_color = 'YlOrRd', 
fill_opacity = 0.7, 
line_opacity = 0.2,
legend_name = 'Neighborhood Incidents',
reset = True)

# display map
world_map
