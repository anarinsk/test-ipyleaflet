#%%
from ipyleaflet import (Map, GeoData, basemaps, WidgetControl, GeoJSON,
 LayersControl, Icon, Marker,basemap_to_tiles, Choropleth,
 MarkerCluster, Heatmap,SearchControl, 
 FullScreenControl)
from ipywidgets import Text, HTML
from branca.colormap import linear
import geopandas as gpd
import json
# %%
# Download link for data https://cloud.comhem.se/s/2252cb28562536544aa85e6019b8ed2faac
# Countries
countries = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# Conflict Dataset Points
africa_acled = gpd.read_file(
 "data/acled2019.shp",
 mask = countries[countries["continent"] == "Africa"]
)
africa_acled.head()
# %%
center = [57.71, 11.98]
zoom = 12
m = Map(basemap=basemaps.Esri.WorldImagery, center=center, zoom=zoom)
m
# %%

# %%
stamen = basemap_to_tiles(basemaps.Stamen.Toner)
m.add_layer(stamen)
# %%
icon_url = "http://icons.iconarchive.com/icons/pelfusion/long-shadow-media/512/Maps-Pin-Place-icon.png"

icon = Icon(icon_url=icon_url)
mark = Marker(location=[57.719503, 12.008843], icon=icon, rotation_angle=0,  rotation_origin='1280px 128px')
m.add_layer(mark);
m
# %%

# %%
