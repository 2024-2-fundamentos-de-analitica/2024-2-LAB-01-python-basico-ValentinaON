"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    diccionario = {}
    with open("files/input/data.csv", mode="r", encoding="utf-8") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")

        for fila in lector_csv:
            if diccionario.get(fila[0]) != None:
                diccionario[fila[0]] += 1
            else:
                diccionario[fila[0]] = 1
    sortedDiccionario = dict(sorted(diccionario.items()))
    return list(sortedDiccionario.items())
