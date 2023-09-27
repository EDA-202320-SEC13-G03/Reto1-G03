"""
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
    """
    # Se adiciona el partido a la lista de partidos

    p = new_partido(partido['date'], partido['home_team'], partido['away_team'],
                    partido['home_score'], partido['away_score'], partido['tournament'],
                    partido['city'], partido['country'], partido['neutral'])

    lt.addLast(catalogo['partidos'], p)

    return catalogo


def add_goleadores(catalogo, goleador):
    """
    Función para agregar nuevos elementos a la lista
    """
    # Se adiciona el goleador a la lista de goleadores

    g = new_goleador(goleador['date'], goleador['home_team'], goleador['away_team'],
                     goleador['team'], goleador['scorer'], goleador['minute'],
                     goleador['own_goal'], goleador['penalty'])

    lt.addLast(catalogo['goleadores'], g)

    return catalogo


def add_penales(catalogo, penales):
    """
    Función para agregar nuevos elementos a la lista
    """
    # Se adiciona la tanda de penales a la lista de penales

    pe = new_penales(penales['date'], penales['home_team'], penales['away_team'],
                     penales['winner'])

    lt.addLast(catalogo['penales'], pe)

    return catalogo

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
    partido['home_score'] = home_score
    partido['away_score'] = away_score
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

def get_1(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pass

def get_2(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pass

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

#para el requerimiento 7
def b_binaria_fecha_incio(data_structs, start):
    
    """Busqueda binaria para encontrar una fecha de inicio"""
    
    min = 1
    max = lt.size(data_structs)

    primero = (lt.firstElement(data_structs))['date']
    ultimo = (lt.lastElement(data_structs))['date']
    
    if start > primero:
        return -1

    #Confirmar que la fecha está en la lista en una posición de la mitad.
    if start >= ultimo:

        #Buscar un día antes para evitar errores al no encontrar la fecha mínima que coincide
        prev = start - timedelta(days=1)

        i = lt.size(data_structs)
        #Busqueda binaria
        while min <= max:
            mitad = (min + max) // 2
            team = lt.getElement(data_structs, min)
            mitad_date = team['date']
            if mitad_date == prev:
                i = mitad
                pass
            elif  mitad_date > prev:
                low = mitad + 1
            else:
                high = mitad - 1
            
            if min == max:
                i = mitad
            i = mitad
                
        encontro = False
        #Iterar hacia atrás para encontrar la primera fecha que coincide
        while not encontro:
            result = lt.getElement(data_structs, i)
            date = result['date']
            if date >= start:
                #Se encuentra la fecha
                return i
            else:
                #Se sigue iterando
                i -= 1

            if i <= 0:
                return -1
    else:
        #Retornar posición de la fecha más antigua
        return lt.size(data_structs)
    
def b_binaria_fecha_final(data_structs, fin):
    
    """Busqueda binaria para encontrar una fecha de inicio"""
    
    min = 1
    max = lt.size(data_structs)

    primero = (lt.firstElement(data_structs))['date']
    ultimo = (lt.lastElement(data_structs))['date']
    
    if fin < primero:
        return -1

    #Confirmar que la fecha está en la lista en una posición de la mitad.
    if fin <= ultimo:

        #Buscar un día despues para evitar errores al no encontrar la fecha mínima que coincide
        sig = fin + timedelta(days=1)

        i = 1
        #Busqueda binaria
        while min <= max:
            mitad = (min + max) // 2
            team = lt.getElement(data_structs, min)
            mitad_date = team['date']
            if mitad_date == sig:
                i = mitad
                pass
            elif  mitad_date > sig:
                low = mitad + 1
            else:
                high = mitad - 1
            
            if min == max:
                i = mitad
            i = mitad
                
        encontro = False
        #Iterar hacia adelante para encontrar la primera fecha que coincide
        while not encontro:
            if i > 0 and i < lt.size(data_structs):

                date = (lt.getElement(data_structs, i))['date']
                if date <= fin:

                    return i
                else:
                    i += 1
            else:
                return 1
    else:
        return 1
    


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


def req_7(data_structs, fecha_ini, fecha_fin, top_jugador):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    
    result=data_structs['partidos']
    
    pos_inicial=b_binaria_fecha_incio(result,fecha_ini)
    pos_fin=b_binaria_fecha_final(result,fecha_fin)
    
    if pos_inicial < pos_fin or pos_inicial == -1 or pos_fin == pos_fin:
        return None,None,None,None,None,None
    
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


def compare_minuto_gol(minute1, minute2):
    
    

    return


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

    merg.sort(catalogo['goleadores'], compare_goleadores)

    pass


def sortpenales(catalogo):
    """
    Función encargada de ordenar la lista con los datos
    """

    merg.sort(catalogo['penales'], compare_goleadores)

    pass
