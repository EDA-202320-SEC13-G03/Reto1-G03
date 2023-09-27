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
 """

import config as cf
import model
import csv
import time
from datetime import datetime

import DISClib as lib

from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs


csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
def new_controller():
    """
    Crea una instancia del modelo
    """
    # TODO: Llamar la función del modelo que crea las estructuras de datos

    control = {'model': None} 
    control['model'] = model.new_data_structs_match() 

    return control

# Funciones para la carga de datos


def load_data(control, tamaño):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    catalogo = control['model']

    partidos = load_partidos(catalogo, tamaño)
    goles = load_goles(catalogo, tamaño)
    penales = load_penales(catalogo, tamaño)

    return partidos, goles, penales

    # abriendo el archivo CSV


def load_partidos(catalogo, tamaño):
    """ 
    Carga el total de partidos jugados en las diferentes competiciones. Se toma
    la informacion de los 3 primeros y 3 ultimos partidos ordenados por la fecha
    del encuentro y el marcador final del partidos.
    Cada partido se compone de:
    
    - Fecha del partido
    - Equipo local.
    - Equipo visitante.
    - Marcador final.
    - Liga a la que está asociado el encuentro.
    - País y ciudad en el que se desarrolló el encuentro.

    cada PÀRTIDO, se crea en la lista de partidos.
   
    """
    if tamaño == "a":
        tamaño = "large"
        
        filename_partidos = cf.data_dir + 'results-utf8-' + tamaño + '.csv'
        input_file = csv.DictReader(open(filename_partidos, encoding='utf-8'))      
        for result in input_file:
            model.add_partido(catalogo, result) 
        
    elif tamaño == "b":
        tamaño = "small"
        
        filename_partidos = cf.data_dir + 'results-utf8-' + tamaño + '.csv'
        input_file = csv.DictReader(open(filename_partidos, encoding='utf-8'))
        for result in input_file:
            model.add_partido(catalogo, result) 
    
    elif tamaño == "small":
        
        tamaño = "small"   
        filename_partidos = cf.data_dir + 'results-utf8-' + tamaño + '.csv'
        input_file = csv.DictReader(open(filename_partidos, encoding='utf-8'))
        for result in input_file:
            model.add_partido(catalogo, result)   
    else:
        raise Exception       

    return model.partidos_size(catalogo)


def load_goles(catalogo, tamaño):
    """
    Carga el total de goles anotados y los jugadores que marcaron gol. Se toma
    la informacion de las 3 primeras y 3 ultimas anotaciones ordenadas por la fecha
    del encuentro, minuto en qué se anotó y el nombre del jugador.
    Cada anotación se compone de:
    
    - Fecha del partido
    - Equipo local.
    - Equipo visitante.
    - Nombre del jugador que marcó el gol.
    - Equipo al que pertenece el jugador.
    - Minuto en que se marcó el gol.
    - Si el gol fue hecho desde el punto penal.
    - Si el gol fue producto de un autogol.

    cada anotación, se crea en la lista de goles.
    """
    if tamaño == "a":
        tamaño = "large"
    elif tamaño == "b":
        tamaño = "small"
    else:
        
        filename_goals = cf.data_dir + 'goalscorers-utf8-' + tamaño + '.csv'
        input_file = csv.DictReader(open(filename_goals, encoding='utf-8'))
        for goal in input_file:
            model.add_goleadores(catalogo, goal)
            
    return model.goleadores_size(catalogo)


def load_penales(catalogo, tamaño):
    """
    Carga el total de penales convertidos en las diferentes competiciones. Se toma
    la informacion de las 3 primeras y 3 ultimas tandas de penal ordenadas por la fecha
    del encuentro y los nombres de los equipos involucrados.
    
    Cada tanda de penales se compone de:
    
    - Fecha del partido
    - Equipo local.
    - Equipo visitante.
    - Equipo ganador.

    cada tanda de penales, se crea en la lista de penales. 
    """
    if tamaño == "a":
        tamaño = "large"
    elif tamaño == "b":
        tamaño = "small"
    else:
        filename_penales = cf.data_dir + 'shootouts-utf8-' + tamaño + '.csv'
        input_file = csv.DictReader(open(filename_penales, encoding='utf-8'))
        for penal in input_file:
            model.add_penales(catalogo, penal)

    return model.penales_size(catalogo)

# Funciones de ordenamiento


def sortpartidos(control):
    """
    Ordena los datos del modelo
    """
  
    partidos_ordenados = model.sortpartidos(control['model'])
    
    return partidos_ordenados


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    # TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, N, equipo, condicion):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    tiempo1=get_time()
    sublista, total_partidos= model.req_1(control, N, equipo, condicion)
    tiempo2=get_time()
    time_fin=delta_time(tiempo1,tiempo2)
    return sublista, total_partidos,time_fin

def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control,n_torneo, fecha_ini, fecha_fin):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    ini = datetime.strptime(fecha_ini, "%Y-%m-%d")
    fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    tiempo1 = get_time()
    if fin >= ini:
        tabular_fin_partidos, ciudades, paises, total_partidos, penaltis = model.req_4(control, n_torneo, ini, fin)
        tiempo2 = get_time()
        time_fin=delta_time(tiempo1,tiempo2)
    return tabular_fin_partidos, ciudades, paises, total_partidos, penaltis, time_fin 


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass


def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    tiempo1=get_time()
    result= model.req_7(control['model'],fecha_ini,fecha_fin,top_jugador)
    tiempo2=get_time()
    time_fin=delta_time(tiempo1,tiempo2)
    return time_fin,result


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass

def goles_de_penal(control, gol):
    """
    Retorna los libros que fueron etiquetados con el tag
    """
    return model.total_goles_penal(control["model"], gol)

def partidos_size(control):
    """
    Retorna el número de partidos
    """
    return model.partidos_size(control["model"])


def goleadores_size(control):
    """
    Retorna el número de goleadores
    """
    return model.goleadores_size(control["model"])

def penales_size(control):
    """
    Retorna el número de penales
    """
    return model.penales_size(control["model"])

# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
