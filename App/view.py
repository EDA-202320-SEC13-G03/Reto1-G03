"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from tabulate import tabulate

from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu


assert cf

# from tabulate import tabulate

# import traceback

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

# numero de elementos para imprimir registros
NTH = 3

"""
La vista se encarga de la interacción con el usuario.

Presenta el menu de opciones y por cada seleccion se hace la solicitud al controlador para ejecutar la
operación solicitada.
"""


def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.new_controller()
    return control


def print_menu_usuario():
    
    """
    Menú de selección de usuario
    """
    print("-------------------\n")
    print("Bienvenido! \n")
    print("Estás a un paso de adentrarte a la historia de las competiciones organizadas por la FIFA. \n")
    print("Para gozar de una mejor experiencia, por favor indica tú tipo de usuario: \n")
    
    print ("1- Soy Estudiante")
    print ("2- Soy parte del Equípo Docente \n")
    
def print_menu_Estudiante(): 
    
    """
    Menú de Estudiante
    """
    print("-------------------\n")
    print("Bienvenido Colega \n")
    
    print("1- Carga la información de las competiciones")
    
    print("2- Análisis de los ultimos partidos de algún equipo")
    print("3- Análisis de los primeros goles anotados por un jugador")
    print("4- Análisis de los partidos disputados por un equipo en un tiempo específico")
    print("5- Análisis de la información de los torneos")
    print("6- Análisis de la capacidad goleadora de un jugador específico")
    print("7- Análisis de los mejores equipos de los torneos")
    print("8- Análisis de los mejores goleadores de los torneos")
    print("9- Análisis del desempeño historico entre selecciones")
    
    print("0- Salir \n")    
    
def print_menu_Docente(): 
    
    """
    Menú del equípo docente
    """
    
    print("Bienvenid@(s) Daniel, Miguel y/o Alejandra \n ")    
    
    print("1- Cargar la información de las competiciones")
    
    print("2- Análisis de los ultimos partidos de algún equipo")
    print("3- Análisis de los primeros goles anotados por un jugador")
    print("4- Análisis de los partidos disputados por un equipo en un tiempo específico")
    print("5- Análisis de la información de los torneos")
    print("6- Análisis de la capacidad goleadora de un jugador específico")
    print("7- Análisis de los mejores equipos de los torneos")
    print("8- Análisis de los mejores goleadores de los torneos")
    print("9- Análisis del desempeño historico entre selecciones")
    
    print("0- Salir \n")
    print("-------------------\n")


def loadData1(control,tamaño):
    """
    Solicita al controlador que cargue los datos en el modelo de los goles.
    """
    results = controller.load_data(control,tamaño)[0]
   
    return results

def loadData2(control,tamaño):
    """
    Solicita al controlador que cargue los datos en el modelo, la carga de los partidos.
    """
    goalscorers = controller.load_data(control, tamaño)[1]
    return goalscorers

def loadData3(control,tamaño):
    """
    Solicita al controlador que cargue los datos en el modelo, la carga de los penales.
    """
    shootouts = controller.load_data(control, tamaño)[2]
    return shootouts

def print_partidos_ordenados(partido, N=NTH):
    # Crear una lista de listas para los datos de la tabla
    partidos_ordenados = controller.sortpartidos(partido)
    
    headers = ["date", "home_team", "away_team", "home_score", 
               "away_score", "tournament", "city", "country"] 
         
    data = [[partido["date"], partido["home_team"], partido["away_team"],
             partido["home_score"],partido["away_score"], partido["tournament"], 
             partido["city"], partido["country"], partido["neutral"]] for partido in partidos_ordenados[:N]]
        
    print(tabulate(data, headers, tablefmt="grid"))

def print_data(lista, N = NTH):
    """
        Función que imprime un dato dado su ID.
    """
    headers = ["date", "home_team", "away_team", "home_score", "away_score", "tournament", "city", "country"]
    size = controller.partidos_size(lista)
    iterator = lt.iterator(lista)
    partidos_ordenados = controller.sortpartidos(lista)
    
    if size <= N*2:
        print(size)
        for partido in iterator:
            
                table =[[partido["date"], partido["home_team"], partido["away_team"],
                partido["home_score"],partido["away_score"], partido["tournament"], 
                partido["city"], partido["country"]] for partido in partidos_ordenados]
                
                print(tabulate(table, headers = 'firstrow', tablefmt='github', showindex=True))
    else:
        print(N)
        i = 1
        while i <= N:
            
            partido = lt.getElement(lista, i)
            
            table=[[partido["date"], partido["home_team"], partido["away_team"],
            partido["home_score"],partido["away_score"], partido["tournament"], 
            partido["city"], partido["country"]] for partido in partidos_ordenados]
                
            print(tabulate(table, headers = 'firstrow', tablefmt='github', showindex=True))
            i += 1 
                   
        print("Los", N, "últimos libros ordenados son:")
        i = size - N + 1
        
        while i <= size:
            partido = lt.getElement(lista, i)
            
            table=[[partido["date"], partido["home_team"], partido["away_team"],
                  partido["home_score"],partido["away_score"], partido["tournament"], 
                  partido["city"], partido["country"]] for partido in partidos_ordenados]
            
            print(tabulate(table, headers = 'firstrow', tablefmt='github', showindex=True))
            i += 1


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    N=int(input("Ingrese el numero de partidos a buscar: "))
    equipo=input("Ingrese el nombre del equipo a buscar")
    condicion=input("Ingrese si el equipo es visitante o local: ")
    sublista, total_partidos,time_fin=controller.req_1(control, N, equipo, condicion)


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    print("////////////busqueda de equipos/////////")
    
    fecha_ini=input("Ingresa la primera fecha Inicial: ")
    
    fecha_fin=input("Ingresa la segunda fecha Final: ")
    
    n_torneo=input("Ingresa el nombre del torneo: ")
    
    tabular_fin_partidos, ciudades, paises, total_partidos, penaltis, time_fin =controller.req_4(control,n_torneo,fecha_ini,fecha_fin)
    
    print("Partidos totales de {0}: {1} ".format(n_torneo,total_partidos) )
    print("")
    print('Paises totales que participaron en {0}: {1} '.format(n_torneo,paises))
    print("")
    print('ciudades totales que participaron en {0}: {1} '.format(n_torneo, ciudades))
    print("")
    print('total de partidos definidos por penales en el {0}: {1} '.format(n_torneo,penaltis))
    print("")
    
    if tabular_fin_partidos==[]:
        print("no se encontro partidos en el tiempo.")
    else:
        print(tabulate(tabular_fin_partidos[1],headers=tabular_fin_partidos[0],tablefmt="simple_grid"))
    print("el tiempo ejecutado del programa es: ",str(time_fin), 'ms')    

    # Se filtran los datos para que queden en orden como en el pdf 
    

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    fecha_ini=input("ingrese la primera fecha inicial para la busqueda : ")
    fecha_fin=input("infrese la seginda fecha para la busqueda")
    jugador_top=input("Ingrese el nombre del jugador a buscar: ")
    result=controller.req_7(control,fecha_ini,fecha_fin,jugador_top)
    print(result)


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

def escoger_tamaño(tamaño):
    
    if str(tamaño) == "a":
        tamaño_escogido = tamaño
    elif str(tamaño) == "b":
        tamaño_escogido = tamaño
    else:
        print("Opción errónea, vuelva a elegir.\n")
        sys.exit(0) 

    return tamaño_escogido

def escoger_tipo(tipo):
    
    if str(tipo) == "a":
        tipo_escogido = tipo
    elif str(tipo) == "b":
        tipo_escogido = tipo
    else:
        print("Opción errónea, vuelva a elegir.\n")
        sys.exit(0) 
            
    return tipo_escogido

# Se crea el controlador asociado a la vista
control = newController()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    
    #ciclo del menu
    while working:
        
        print_menu_usuario()
        print("-------------------\n")
        inputs = input('Seleccione una opción para continuar\n' + "\n"+"-------------------\n")
        
        if int(inputs) == 1:
            
            print_menu_Estudiante()
            print("-------------------\n")
            inputs = input('Seleccione una opción para continuar\n' + "\n"+"-------------------\n")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                print("-------------------\n")
                data, data2, data3 = loadData1(control,tamaño = 'small'),loadData2(control,tamaño='small'), loadData3(control,tamaño ='small')
                print('se han cargandos los siguientes datos: \n ')
                print("-------------------\n")
                
                headers = ["Tipo", "Total"]
                table=[("Partidos",data), ("Goleadores", data2), ("Goles de penal",data3)]
                print(tabulate(table, headers, tablefmt="simple"))
                print("\n")
                print("-------------------\n")
                print_partidos_ordenados(control,5)
                
            elif int(inputs) == 2:
                print_req_1(control)
            
            elif int(inputs) == 3: 
                print_req_2(control)
            elif int(inputs) == 4:
                print_req_3(control)
                
            elif int(inputs) == 5:
                print_req_4(control)
            
            elif int(inputs) == 6: 
                print_req_5(control)
            
            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)
                
            elif int(inputs) == 9:
                print_req_8(control)
            
            
                
            elif int(inputs) == 0: 
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
                sys.exit(0)     
                                  
        elif int(inputs) == 2:
            
            print_menu_Docente()
            inputs = input('Seleccione una opción para continuar\n')
            
            if int(inputs) == 1:
                print('¿Qué tipo de lista quiere que implemente el programa?\n'+'a. ArrayList\n' + 'b. SingleLinked\n')
                tipo = input('Seleccione una opción para continuar\n')
                tipo_escogido = escoger_tipo(tipo)
                print('¿Qué cantidad de datos desea cargar?\n'+
                      'a. large\n' + 'b. small\n')
                tamaño = input('Seleccione una opción para continuar\n')
                tamaño_escogido = escoger_tamaño(tamaño)
                print("Cargando información de los archivos ....\n")
                data = loadData1(tamaño_escogido),loadData2(tamaño_escogido),loadData3(tamaño_escogido)
                print('se han cargandos los siguientes datos: ')
                print(data[0],'Resultados de los partidos.')
                print(data[1],'Goleadores.')
                print(data[2],'Goles anotados desde el punto de penal.')
                
            elif int(inputs) == 2:
                print_req_1(control)
            
            elif int(inputs) == 3: 
                print_req_2(control)
            
            elif int(inputs) == 4:
                print_req_3(control)
                
            elif int(inputs) == 5:
                print_req_4(control)
            
            elif int(inputs) == 6: 
                print_req_5(control)
            
            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)
                
            elif int(inputs) == 9:
                print_req_8(control)
                
            elif int(inputs) == 0: 
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
                sys.exit(0)                
                
        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
            
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)


