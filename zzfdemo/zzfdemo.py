"""Main module."""

import ipyleaflet
from ipyleaflet import basemaps
class Map(ipyleaflet.Map):
    
    def __init__(self,center=[34.32, 108.55],zoom=4, **kwargs):
        super().__init__(center = center,zoom = zoom ,**kwargs)
        self.add_control(ipyleaflet.LayersControl())
    
    def add_tile_layer(self,url,name , **kwargs):
        layer = ipyleaflet.TileLayer(url = url,name = name ,**kwargs)
        self.add_layer(layer)

    def add_basemap(self,name):
        if isinstance(name,str):
            url = eval(f'basemaps.{name}').build_url()
            self.add_tile_layer(url,name)
        else:
            self.add_layer(name)

    