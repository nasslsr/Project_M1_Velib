#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 00:27:21 2023

@author: nass
"""


import mysql.connector
import requests


my_url='https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json'

# RECUPERATION DES DONNEES DE L'API SUR LES STATIONS
def get_station_information():
    my_url='https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json'

    request_result = requests.get(my_url)
    request_data= request_result.json()
    information_localization = request_data['data']['stations']
      
    final_list=[]  

   
    for data in information_localization:
   
        station_id = data['station_id']
        name = data['name']
        geographic_lat =  data['lat']
        geographic_lon = data['lon']
        capacity = data['capacity']
        stationCode = data['stationCode']
        my_list=[station_id,name,geographic_lat,geographic_lon,capacity,stationCode]
        final_list.append(my_list)
       
        
        
    return final_list



# RECUPERATION DES DONNEES DE L'API SUR LES DISPO DES VELOS STATIONS

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
            
 


#CONNEXION A LA BDD

db= mysql.connector.connect(
   host="localhost",
   port=8889,
   user="root",
   password="root",
   database="Station_Information_Velib"
)

mycursor = db.cursor()


list_of_data = get_station_information()
availability_list = collect_data_availability_velib_terminal(my_url)


#ON RECUP TOUTES LES DONNEES DE L'API POUR LES METTRE DANS LA BDD EN PARCOURANT LA LISTE
"""
sql = "INSERT INTO Station_Information (station_id, name, lat, lon, capacity, stationCode) VALUES (%s, %s, %s, %s, %s, %s)"
for data in list_of_data:
    mycursor.execute(sql, data)
    db.commit()
    
print(mycursor.rowcount, "records inserted.")
"""
    
 
sql = "INSERT INTO Availability_Velib_Terminal (stationCode,station_id,num_bikes_available,numBikesAvailable,num_docks_available,numDocksAvailable,is_installed,is_returning,is_renting ,last_reported) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s,%s)"
for data in availability_list:
    data_tuple = tuple(data.values())
    mycursor.execute(sql, data_tuple)
    db.commit()
    

print(mycursor.rowcount, "records inserted.")
























"""
import requests
import mysql.connector

db = mysql.connector.connect(
    host="localhost", 
    user="root",
    passwd="nasser92",
    
    
    
    )

mycursor = db.cursor()


#mycursor.execute("CREATE DATABASE Station_Information_Velib")

#mycursor.execute("CREATE TABLE Station_Information_Velib (station_id INT PRIMARY KEY, name VARCHAR(255), lat FLOAT, lon FLOAT , capacity INT, stationCode VARCHAR(250))")





def get_station_information():
    my_url='https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json'

    request_result = requests.get(my_url)
    request_data= request_result.json()
    information_localization = request_data['data']['stations']
      
    final_list=[]  

   
    for data in information_localization:
   
        station_id = data['station_id']
        name = data['name']
        geographic_lat =  data['lat']
        geographic_lon = data['lon']
        capacity = data['capacity']
        stationCode = data['stationCode']
        my_list=[station_id,name,geographic_lat,geographic_lon,capacity,stationCode]
        final_list.append(my_list)
       
        
        
    return final_list
    


db = mysql.connector.connect(
    host="localhost", 
    user="root",
    passwd="nasser92",
    database="Station_Information_Velib"
    )

mycursor = db.cursor()


list_of_data = get_station_information()

sql = "INSERT INTO Station_Information_Velib (station_id, name, lat, lon, capacity, stationCode) VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE station_id=station_id"
for data in list_of_data:
    mycursor.execute(sql, data)
    db.commit()

print(mycursor.rowcount, "records inserted.")

















#mycursor.execute("INSERT INTO Station_Information_Velib (station_id, name , lat , lon  , capacity , stationCode) VALUES (station_id,name,lat, lon, capacity, stationCode ) ON DUPLICATE KEY UPDATE station_id=station_id")
   # db.commit()

sql= "INSERT INTO Station_Information_Velib (station_id, name , lat , lon  , capacity , stationCode) VALUES (%d,%s,%f, %f, %d, %s) "
val = List_of_Data
mycursor.execute(sql, val)

db.commit()

print(mycursor.rowcount, "record inserted.")    



sql = "DELETE FROM Station_Information_Velib"

mycursor.execute(sql)
db.commit()

print(mycursor.rowcount, "record(s) deleted")

#mycursor.execute("CREATE TABLE Station_Information (station_id INT PRIMARY KEY, name VARCHAR(255), lat FLOAT, lon FLOAT , capacity INT, stationCode VARCHAR(250))")

#mycursor.execute("CREATE DATABASE Station_Information_Velib")



  
    
#mycursor.execute("SELECT * FROM Station_Information_Velib ")

 #myresult = mycursor.fetchall()

 #for x in myresult:
  # print(x)  


         



mycursor.execute("SHOW DATABASES")

#mycursor.execute("INSERT INTO Person(name,age,personID) VALUES('nass',22,1)")


#mycursor.execute("SELECT * FROM Person")

#for x in mycursor:
   #print(x)
   
   """
