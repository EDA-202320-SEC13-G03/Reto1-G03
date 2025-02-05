﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import datetime
import random

import DISClib as DLIB
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.DataStructures import arraylist as al
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from datetime import timedelta

assert cf

"""
Se define la estructura de un catálogo de la FIFA. El catálogo tendrá
tres listas, una para los partidos, otra para los goleadores y otra para los penales.
"""

# Construccion del modelo


def new_data_structs_match():
    """
    Inicializa el catálogo de la FIFA. 
    Crea listas vacias para guardar la información de los partidos, goleadores y penales.
    Retorna el catalogo inicializado.

    """
    # creando y configurando el ADT list para almacenar los partidos
    # creando y configurando los atributos que componen un partido

    catalogo = {'partidos': None,
                'goleadores': None,
                'penales': None,
                }

    catalogo['partidos'] = lt.newList(
        'ARRAY_LIST', cmpfunction=partido_sort_criteria)
    catalogo['goleadores'] = lt.newList(
        'ARRAY_LIST', cmpfunction=compare_goleadores)
    catalogo['penales'] = lt.newList(
        'ARRAY_LIST', cmpfunction=compare_penales)

    return catalogo


# Funciones para agregar informacion al modelo

def add_partido(catalogo, partido):
    """
    Función para agregar nuevos partidos a la lista
    
    catalogo: Recibe la lista donde se van a añadir los datos, en este caso
              catalogo['partidos']
    partido: Recibe el partido (tipo diccionario) que se va a añadir en
             la lista partidos ubicada en el catalogo
    
    """
    # Se adiciona el partido a la lista de partidos

    p = new_partido(partido['date'], partido['home_team'], partido['away_team'],
                    partido['home_score'], partido['away_score'], partido['tournament'],
                    partido['city'], partido['country'], partido['neutral'])

    lt.addLast(catalogo['partidos'], p)



def add_goleadores(catalogo, goleador):
    """
    Función para agregar nuevos elementos a la lista
    """
    # Se adiciona el goleador a la lista de goleadores

    g = new_goleador(goleador['date'], goleador['home_team'], goleador['away_team'],
                     goleador['team'], goleador['scorer'], goleador['minute'],
                     goleador['own_goal'], goleador['penalty'])

    lt.addLast(catalogo['goleadores'], g)



def add_penales(catalogo, penales):
    """
    Función para agregar nuevos elementos a la lista
    """
    # Se adiciona la tanda de penales a la lista de penales

    pe = new_penales(penales['date'], penales['home_team'], penales['away_team'],
                     penales['winner'])

    lt.addLast(catalogo['penales'], pe)


# Funciones para creacion de datos


def new_partido(date, home_team, away_team, home_score, away_score, tournament, city, country, neutral):
    """
    Crea una nueva estructura para modelar los datos
    """
    
    
    
    partido = {'date': "", 'home_team': "", 'away_team': "", 'home_score': 0, 'away_score': 0,
               'tournament': "", 'city': "", 'country': "", 'neutral': ""}

    partido['date'] = date
    partido['home_team'] = home_team
    partido['away_team'] = away_team
    partido['home_score'] = int(home_score)
    partido['away_score'] = int(away_score)
    partido['tournament'] = tournament
    partido['city'] = city
    partido['country'] = country
    partido['neutral'] = neutral

    return partido



def new_goleador(date, home_team, away_team, team, scorer, minute, own_goal, penalty):
    """
    Crea una nueva estructura para modelar los datos
    """
    goleador = {'date': "", 'home_team': "", 'away_team': "", 'team': "",
                'scorer': "", 'minute': 0, 'own_goal': None, 'penalty': None}

    goleador['date'] = date
    goleador['home_team'] = home_team
    goleador['away_team'] = away_team
    goleador['team'] = team
    goleador['scorer'] = scorer
    goleador['minute'] = minute
    goleador['own_goal'] = own_goal
    goleador['penalty'] = penalty

    return goleador

def new_penales(date, home_team, away_team, winner):
    """
    Crea una nueva estructura para modelar los datos
    """
    penales = {'date': "", 'home_team': "", 'away_team': "", 'winner': ""}

    penales['date'] = date
    penales['home_team'] = home_team
    penales['away_team'] = away_team
    penales['winner'] = winner
    
    return penales


# Funciones de consulta

def primeros_y_ultimos(catalogo):
    """
    Retorna los 3 primero y 3 ultimos a partir de un criterio de ordenamiento
    """
    lista = lt.newList('ARRAY_LIST')
    
    for result in catalogo:
        
        if result == "partidos":
           sublista = catalogo[result]
           index = lt.size(sublista) -1
           merg.sort(sublista,partido_sort_criteria)
           
        elif result == "goleadores":   
            sublista = catalogo[result]
            index = lt.size(sublista) -1
            merg.sort(sublista,compare_goleadores)
            
        elif result == "penales":
            sublista = catalogo[result]
            index = lt.size(sublista) -1
            merg.sort(sublista,compare_penales)    
           
        for pos in range(3):
            primero = lt.getElement(sublista, pos)
            ultimo = lt.getElement(sublista, index - pos)
            lt.addFirst(lista, primero)
            lt.addLast(lista, ultimo)
                  
    return lista

def primeros_y_ultimos(sublista):
    """
    Retorna los 3 primero y 3 ultimos a partir de un criterio de ordenamiento
    """
    lista = lt.newList('ARRAY_LIST')
    
    for contenido in lt.iterator(sublista):
        index = lt.size(sublista)
        for pos in range(1,3):
            primero = lt.getElement(sublista, pos)
            ultimo = lt.getElement(sublista, index - pos)
            lt.addFirst(lista, primero)
            lt.addLast(lista, ultimo)
            merg.sort(lista, criterio)
               
    return lista

def ultimos_partidos_equipo_condicion(catalogo, N, equipo, condicion): #Requerimiento 1
    
    partidos = catalogo['partidos']
    sublista = lt.newList()
    total_local= 0
    total_visitante = 0
    total_partidos = 0
    
    for contenido in lt.iterator(partidos):
        
        if condicion == "local":
            
            if contenido['home_team'] == equipo:
                total_local += 1
                total_partidos += 1
                 
        elif condicion == "vistante":
            
            if contenido['away_team'] == equipo:
                 total_visitante += 1
                 total_partidos += 1 
        elif condicion == "indiferente":
            if  contenido['home_team'] == equipo or contenido['away_team'] == equipo : 
                total_partidos += 1   
                    
    lt.addLast(sublista,contenido)    
    
    return sublista, total_partidos

def primeros_N_goles_jugador(catalogo, N, jugador): #Requerimiento 2

    """
    Retorna los N primeros goles de un jugador 
    """
    goleadores = catalogo['goleadores']
    lista = lt.newList('ARRAY_LIST')
    sublista = lt.newList('ARRAY?LIST')
    total = 0
    
    for contenido in lt.iterator(goleadores):
        if contenido['scorer'] == jugador:
           lt.addLast(lista,contenido)
           total += 1
        
           index = lt.size(lista) -1
           merg.sort(lista, compare_fecha_minuto_gol)
           for pos in range(N):
               primeros = lt.getElement(lista, pos)
               lt.addLast(sublista, primeros)
               
    return sublista, total    

def obtener_partidos_equipo_por_periodo(catalogo, equipo, fecha_inicial, fecha_final): # Requerimiento 3
    """
    Retorna una lista de datos a partir de in periodo definido
    """
    partidos = catalogo['partidos']
    sublista = lt.newList('ARRAY_LIST')
    total = 0
    
    for contenido in lt.iterator(partidos):
        if contenido['home_team'] or contenido['away_team'] == equipo:
            if int(contenido['date']) >= fecha_inicial and int(contenido['date']) <= fecha_final:
                lt.addLast(sublista,contenido)
                total +=1
    return sublista, total  

def obtener_partidos_torneo_por_periodo(catalogo, torneo, fecha_inicial, fecha_final): # Requerimiento 3
    """
    Retorna una lista de datos a partir de in periodo definido
    """
    partidos = catalogo['partidos']
    penales = catalogo['penales']
    
    sublista = lt.newList('ARRAY_LIST')
    
    total_partidos = 0
    total_paises = 0
    total_penales = 0
    total_ciudades = 0
    total_tandas_penal = 0

    
    for contenido in lt.iterator(partidos):
        for contenido_penales in lt.iterator(penales):
            if contenido['home_team'] or contenido['away_team'] == equipo:
                if int(contenido['date']) >= fecha_inicial and int(contenido['date']) <= fecha_final:
                lt.addLast(sublista,contenido)
                total +=1
    return sublista, total  

def obtener_goles_jugador_por_periodo(catalogo, nombre, fecha_inicial, fecha_final): # Requerimiento 5
    """
    Retorna una lista de datos a partir de in periodo definido
    """
    partidos = catalogo['goleadores']
    sublista = lt.newList('ARRAY_LIST')
    total_goles = 0
    # total_torneos = 0
    total_penales = 0
    total_autogoles =0
    
    for contenido in lt.iterator(partidos):
        if contenido['scorer'] == nombre:
            if int(contenido['date']) >= fecha_inicial and int(contenido['date']) <= fecha_final:
               
               if contenido['penalty'] == True:
                   total_penales += 1
               elif contenido['autogol'] == True:
                   total_autogoles += 1   

            lt.addLast(sublista,contenido)
            total_goles +=1

    return sublista, total_goles, total_autogoles, total_penales
  

def get_3(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pass

def get_4(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pass

def total_goles_penal(catalogo, gol):
    
    goles_de_penal = catalogo['goleadores']
    contador = 0
    
    pos = lt.isPresent(goles_de_penal, gol)
    
    if pos > 0:
        gol_de_penal = lt.getElement(goles_de_penal, pos)
        if gol_de_penal is not None:
            for g in lt.iterator(catalogo["goleadores"]):
                if gol_de_penal["penalty"] == g["penalty"]:
                    contador += 1
    return contador

def partidos_size(catalogo):
    """
    Retorna el tamaño de la lista de los partidos
    """
    partidos = catalogo['partidos']
    return lt.size(partidos)


def goleadores_size(catalogo):
    """
    Retorna el tamaño de la lista de los goleadores
    """
    goles = catalogo['goleadores']
    return lt.size(goles)


def penales_size(catalogo):
    """
    Retorna el tamaño de la lista de los penales
    """
    penales = catalogo['penales']
    return lt.size(penales)


    


# Implementación de requerimientos

def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structure, n_torneo, fecha_ini, fecha_fin):
    """Partidos relacionados con un torneo durante un periodo específico"""

    
    lista_partidos = data_structure["partidos"]
    lista_penales = data_structure["penales"]
    #partidos y penales general
    list_fin_partidos = lt.newList("ARRAY_LIST")
    list_fin_penales = lt.newList("ARRAY_LIST")
    #paises y ciudades de los encuentros
    lt_ciudad = lt.newList("ARRAY_LIST")
    lt_paises = lt.newList("ARRAY_LIST")

    for date in lt.iterator(lista_partidos):
        fecha_part = date["date"]
        
        if fecha_part <= fecha_fin and fecha_part >= fecha_ini and date["tournament"] == n_torneo:
            date["winner"] = "unknown"
            lt.addLast(list_fin_partidos, date)

    for date in lt.iterator(lista_penales):
        fecha_penal = date["date"]
        
        if fecha_penal <= fecha_fin and fecha_penal >= fecha_ini:
            lt.addLast(list_fin_penales, date)

    penales = 0
    for i in lt.iterator(list_fin_penales):
        for dato_part in lt.iterator(list_fin_partidos):
            if i["home_team"] == dato_part["home_team"] and i["away_team"] == dato_part["away_team"]:
                penales += 1
                dato_part["winner"] = i["winner"]

    for i in lt.iterator(list_fin_partidos):
        ciudad_dato = i["city"]
        pais_dato = i["country"]
        if not lt.isPresent(lt_ciudad, ciudad_dato):
            lt.addLast(lt_ciudad, ciudad_dato)
        if not lt.isPresent(lt_paises, pais_dato):
            lt.addLast(lt_paises, pais_dato)

    num_ciudades = lt.size(lt_ciudad)
    num_paises = lt.size(lt_paises)
    total_partidos = lt.size(list_fin_partidos)
    
    tabular_fin_partidos=tabulate_add_req4(list_fin_partidos)

    return tabular_fin_partidos, num_ciudades, num_paises, total_partidos, penales

def tabulate_add_req4(data_structure):
    orden= lt.size(data_structure)
    if orden == 0:
        lista=[]
    else:
        titulos= list(lt.getElement(data_structure, 2).keys())
        
        elemento=list(lt.getElement(data_structure,1).values())
        elemento2=list(lt.getElement(data_structure,2).values())
        elemento3=list(lt.getElement(data_structure,3).values())
        
        elemento4=list(lt.getElement(data_structure,orden-2).values())
        elemento5=list(lt.getElement(data_structure,orden-1).values())
        elemento6=list(lt.getElement(data_structure,orden).values())
        
        lista= titulos,[elemento,elemento2,elemento3,elemento4,elemento5,elemento6]
        
    return lista

def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(catalogo, fecha_ini, fecha_fin, top_jugador):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    
    result=catalogo['partidos']
    total_anotadores = 0
    total_torneos= 0 
    total_goles = 0 
    goles_penal = 0
    total_autogol = 0
     
    
    torneosP=lt.newList(datastructure='ARRAY_LIST')
    
    total_partidos = 0
    num_goles = 0
    num_penales = 0
    num_autogoles = 0
    
    for partido in lt.iterator(data_structs['partidos']):
        if partido['date'] <= fecha_ini and partido['date'] >= fecha_fin and partido['tournament'] != "Friendly":
            lt.addLast(torneosP, partido)
    
    print(torneosP)
    
            
    
    #tabulate(agrgar)
    
    
    


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista


def compare_date(date1, date2):
    """
    Función encargada de comparar dos datos
    """
    date1 = datetime.datetime.strptime(date1["date"], "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date2["date"], "%Y-%m-%d")   
     
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    
    return -1


def compare_score(home_score_1, away_score_1, home_score_2, away_score_2):
    
    if home_score_1 < home_score_2:
            return True
    elif home_score_1 == home_score_2:
             return away_score_1 < away_score_2
    return False


def compare_fecha_minuto_gol(goleador1, goleador2):
    
    date1 = datetime.datetime.strptime(goleador1["date"], "%Y-%m-%d")
    date2 = datetime.datetime.strptime(goleador2["date"], "%Y-%m-%d")
    
    if date1 < date2:
        return True
    elif date1 == date2:
        if goleador1["minute"] < goleador2["minute"]:
            return True
    return False

    


def compare_nombre_goleador(nombre1, nombre2):

    return

#req7
def comparar_name(team1,team2):
    
    t1 = team1.lower()
    t2 = team2['name'].lower()

    if t1 > t2:
        return 1
    elif t1 < t2:
        return -1
    else:
        return 0


# Funciones de comparación para el ordenamiento


def compare_goleadores(goleador1_, goleador2):

    return


def compare_penales(penales1,penales2):

    return


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
   
    pass

def partido_sort_criteria(partido1, partido2):
    
    date1 = datetime.datetime.strptime(partido1["date"], "%Y-%m-%d")
    date2 = datetime.datetime.strptime(partido2["date"], "%Y-%m-%d")
    
    if date1 < date2:
        return True
    elif date1 == date2:
        if partido1["home_score"] < partido2["home_score"]:
            return True
        elif partido1["home_score"] == partido2["home_score"]:
            return (partido1["away_score"] < partido2["away_score"])
    return False

# Funciones de ordenamiento

def sortpartidos(catalogo):
    """
    Función encargada de ordenar la lista con los datos
    """
    partidos = catalogo["partidos"]
    lista_ordenada = merg.sort(partidos, partido_sort_criteria)
    catalogo["partidos"] = lista_ordenada
    
    return lista_ordenada


def sortgoleadores(catalogo):
    """
    Función encargada de ordenar la lista con los datos
    """

    goleadores = merg.sort(catalogo['goleadores'], compare_goleadores)

    return goleadores


def sortpenales(catalogo):
    """
    Función encargada de ordenar la lista con los datos
    """

    penales = merg.sort(catalogo['penales'], compare_goleadores)

    return penales
