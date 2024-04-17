#!/usr/bin/env python
# coding: utf-8

# In[169]:


import pandas as pd
import statistics

miasta = [
    'wroclaw',
    'torun',
    'lublin',
    'zielonagora',
    'lodz',
    'krakow',
    'warszawa',
    'opole',
    'rzeszow',
    'bialystok',
    'gdansk', 
    'katowice',
    'kielce',
    'olsztyn',
    'poznan', 
    'szczecin'
]

def pobierz_dane():
    temperatury = []
    opady = []
    cisnienia = []
    stacja_min_temp = None
    min_temp = float('inf')
    max_temp = float('-inf')
    min_opad= float('inf')
    max_opad = float('-inf')
    min_cis= float('inf')
    max_cis = float('-inf')
    
    for miasto in miasta:
        url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}"
        response = requests.get(url, verify=True)
        if response.status_code != 200:
            raise Exception('Failed to load page {}'.format(url))
        
        data = response.json()
#         print(data)
        temperatura = float(data['temperatura'])
        temperatury.append(temperatura)
        
        opad = float(data['suma_opadu'])
        opady.append(opad)
        
        cisnienie = float(data['cisnienie'])
        cisnienia.append(cisnienie)
        
        if temperatura < min_temp:
            min_temp = temperatura
            stacja_min_temp = data['stacja']

        if temperatura > max_temp:
            max_temp = temperatura
            stacja_max_temp = data['stacja']
        if opad < min_opad:
            min_opad = opad
            stacja_min_opad = data['stacja']
        if opad > max_opad:
            max_opad = opad
            stacja_max_opad = data['stacja']
        if cisnienie < min_cis:
            min_cis = cisnienie
            stacja_min_cis = data['stacja']
        if cisnienie > max_cis:
            max_cis = cisnienie
            stacja_max_cis = data['stacja']
            
            
            
    srednia_temp = statistics.mean(temperatury)
    srednie_opady = statistics.mean(opady)
    srednie_cisn = statistics.mean(cisnienia)
    data_pomiaru = data['data_pomiaru']
    godzina_pomiaru = data['godzina_pomiaru']
    
    print("Średnia temperatura punktów pomiarowych:", round(srednia_temp, 2), "°C")
    print("Minimalna temperatura:", min_temp, "°C w miejscu pomiaru:", stacja_min_temp)
    print("Maksymalna temperatura:", max_temp, "°C w miejscu pomiaru:", stacja_max_temp)
    print("Data pomiaru:", data_pomiaru, "godzina pomiaru:", godzina_pomiaru)
    print("Średnia wartość opadów:", round(srednie_opady, 2), "mm")
    print("Minimalna wartość opadów:", min_opad, "mm w miejscu pomiaru:", stacja_min_opad)
    print("Maksymalna wartość opadów:", max_opad, "mm w miejscu pomiaru:", stacja_max_opad)
    print("Średnia wartość ciśnienia:", round(srednie_cisn, 2), "hPa")
    print("Minimalna wartość ciśnienia:", min_cis, "hPa w miejscu pomiaru:", stacja_min_cis)
    print("Maksymalna wartość ciśnienia:", max_cis, "hPa w miejscu pomiaru:", stacja_max_cis)
    
    with open("dane_pogodowe.txt", "w") as file:
        file.write("Średnia temperatura punktów pomiarowych: " + str(round(srednia_temp, 2)) + " °C\n")
        file.write("Minimalna temperatura: " + str(min_temp) + " °C w miejscu pomiaru: " + stacja_min_temp + "\n")
        file.write("Maksymalna temperatura: " + str(max_temp) + " °C w miejscu pomiaru: " + stacja_max_temp + "\n")
        file.write("Data oraz godzina pomiaru: " + str(data_pomiaru) + str(godzina_pomiaru) + "\n")
        file.write("Średnia wartość opadów: " + str(round(srednie_opady, 2)) + " mm\n")
        file.write("Minimalna wartość opadów: " + str(min_opad) + " mm w miejscu pomiaru: " + stacja_min_opad + "\n")
        file.write("Maksymalna wartość opadów: " + str(max_opad) + " mm w miejscu pomiaru: " + stacja_max_opad + "\n")
        file.write("Średnia wartość ciśnienia: " + str(round(srednie_cisn, 2)) + " hPa\n")
        file.write("Minimalna wartość ciśnienia: " + str(min_cis) + " hPa w miejscu pomiaru: " + stacja_min_cis + "\n")
        file.write("Maksymalna wartość ciśnienia: " + str(max_cis) + " hPa w miejscu pomiaru: " + stacja_max_cis + "\n")
    
pobierz_dane()

