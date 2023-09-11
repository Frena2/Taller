#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:08:35 2023

@author: fernandogarcia-galindo
"""

import requests
response_iss = requests.get("http://api.open-notify.org/iss-now.json").json()
lat_iss = float(response_iss["iss_position"]["latitude"])
lon_iss = float(response_iss["iss_position"]["longitude"])

response_etsidi = requests.get( "https://geocode.maps.co/search?q=Ronda+Valencia+3+MADRID" ).json()
lat_etsidi = float(response_etsidi[0]["lat"])
lon_etsidi = float(response_etsidi[0]["lon"])

print( f"La ISS está a {lat_etsidi-lat_iss:.2f}º latitud y a {lon_etsidi-lon_iss:.2f}º longitud") 
