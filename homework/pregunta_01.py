"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    contador = 0
    with open("files/input/data.csv", mode="r", encoding="utf-8") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")

        for fila in lector_csv:
            contador += int(fila[1])  # Segunda columna

    return contador
