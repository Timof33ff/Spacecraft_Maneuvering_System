import numpy as np
import pandas as pd

from math import *

# Начальные параметры
G = 6.67430e-11  # Гравитационная постоянная
M_star = 1.989e30  # Масса звезды (Солнце)
M_planet = 5.972e24  # Масса планеты (Земля)
radius = 6400e3  # Радиус Земли (м)

# Параметры орбиты Земли
semi_major_axis_earth = 1.0  # Большая полуось в астрономических единицах
eccentricity_earth = 0.0167  # Эксцентриситет орбиты Земли

# Временные параметры
t_max = 3.154e7 * 1  # Год в секундах (один земной год)
dt = 3600  # Шаг итерации (один час)

def GravityForce(mass1 : float, mass2 : float, R : float) -> float:
    return (G*mass1*mass2)/pow(R, 2)

class MModel():
    def __init__(self):
        pass
