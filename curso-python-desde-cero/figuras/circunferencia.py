"""Modulo circunferencia:
Incluye las funciones que nos permiten obtener el perímetro o
área de una circunferencia.
"""


import math


def perimetro(radio):
    return 2 * math.pi * radio


def area(radio):
    return math.pi * radio ** 2