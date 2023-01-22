import folium
import pandas as pd
from folium import LayerControl
from folium.plugins import LocateControl, Fullscreen, Geocoder, MarkerCluster


def create_map():
    my_map = folium.Map(
        location=[56.28014473079744, 43.97535907222193],
        zoom_start=11,
        tiles=None,
    )
    folium.TileLayer("OpenStreetMap", name='Город').add_to(my_map)

    folium.TileLayer(
        'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        name='Спутник',
        attr='Esri.WorldImagery',
    ).add_to(my_map)

    marker_cluster = MarkerCluster()
    offices_marker_cluster = folium.FeatureGroup(name='Офисы').add_to(my_map)

    df_office = pd.read_csv('map/get_data/bank_office.csv')
    icon = "fa-building"
    for i in range(len(df_office)):
        locations = [df_office.iloc[i]['latitude'], df_office.iloc[i]['longitude']]
        marker_cluster.add_child(
            folium.Marker(
                locations,
                popup=f"""
                        <h3><b>Сбербанк</b></h3>
                        <p>Офис</p>
                         {df_office.iloc[i]['address']}""",
                icon=folium.Icon(icon=icon, prefix='fa', color='blue'),
            )
        ).add_to(offices_marker_cluster)

    atm_marker_cluster = folium.FeatureGroup(name='Банкоматы', show=False).add_to(my_map)

    marker_cluster = MarkerCluster()

    df_atm = pd.read_csv('map/get_data/bank_atm.csv')
    icon = "fa-rub"
    for i in range(len(df_atm)):
        locations = [df_atm.iloc[i]['latitude'], df_atm.iloc[i]['longitude']]
        marker_cluster.add_child(
            folium.Marker(
                locations,
                popup=f"""
                        <h3><b>Сбербанк</b></h3>
                        <p>Банкомат</p>
                         {df_atm.iloc[i]['address']}""",
                icon=folium.Icon(icon=icon, prefix='fa', color='green')
            )
        ).add_to(atm_marker_cluster)

    Fullscreen().add_to(my_map)
    LocateControl().add_to(my_map)
    Geocoder().add_to(my_map)
    LayerControl().add_to(my_map)
    return my_map._repr_html_()
