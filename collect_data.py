#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:56:13 2023

@author: nass
"""
import requests
import folium




my_url='https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json'


def collect_data_localization(my_url):
    
    
    request_result = requests.get(my_url)
    request_data= request_result.json()
    
    information_localization = request_data['data']['stations']
  
    data_localization_information=[]
    
    for data in information_localization:
            data_localization = {"station_id" : data['station_id'],
                                     "name" : data['name'],
                                    "geographic_lat" : data['lat'],
                                    "geographic_lon" :  data['lon'],
                                    "capacity" : data['capacity'],
                                     "stationCode" : data['stationCode']}
            data_localization_information.append(data_localization)
            
          
    return data_localization_information

localization_list =  collect_data_localization(my_url)
print(localization_list)
    
    
def collect_geographic_coordinates(my_url):
    
    request_result = requests.get(my_url)
    request_data= request_result.json()
    
    information_stations = request_data['data']['stations']
  
    geographic_coordinates=[]
    
    for data in information_stations:
       coordinates = {"geographic_lat": data['lat'], "geographic_lon": data['lon']}
       geographic_coordinates.append(coordinates)
       
    return geographic_coordinates


coordinates_list = collect_geographic_coordinates(my_url)
print(coordinates_list)

  

            
        
        
        
my_url='https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json'

def collect_data_availability_velib_terminal(my_url):    
    
    request_result = requests.get(my_url)
    request_data= request_result.json()
    
    information_stations = request_data['data']['stations']
  
    data_availability_information=[]
    
    for data in information_stations:
            data_availability = {"stationCode" : data['stationCode'],
                                "station_id" : data['station_id'],
                                "num_bikes_available" : data['num_bikes_available'],
                                    "numBikesAvailable" : data['numBikesAvailable'],
                                    "num_bikes_available_types" :  data['num_bikes_available_types'],
                                    "num_docks_available" : data['num_docks_available'],
                                     "numDocksAvailable" : data['numDocksAvailable'],
                                     "is_installed" : data['is_installed'],
                                     "is_returning" : data['is_returning'],
                                     "is_renting" : data['is_renting'],
                                     "last_reported" : data['last_reported']}
            data_availability_information.append(data_availability)
            
    return data_availability_information
            
availability_list = collect_data_availability_velib_terminal(my_url)   
print(availability_list) 
        

    
#afficher la map avec la bibli folium avec tous les reperes

# Création de la carte centrée sur la première paire de coordonnées donc l'adresse dans le 16eme
map = folium.Map(location=[coordinates_list[0]["geographic_lat"], coordinates_list[0]["geographic_lon"]], zoom_start=10)



# Boucle pour parcourir la liste de coordonnées et créer des repères pour chaque paire de coordonnées
for coord in coordinates_list:
        lat = coord["geographic_lat"]
        lon = coord["geographic_lon"]
        folium.Marker([lat, lon],).add_to(map)


# Affichage de la carte
map


    
    
    
    
    
