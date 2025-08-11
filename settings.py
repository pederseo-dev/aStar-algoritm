import pygame
from matriz import Mapa


#datos de la matriz
MAPA_AUTO = Mapa.mapa_auto
MAPA = Mapa.mapa
FILAS = len(MAPA)
COLUMNAS = len(MAPA[0])

# Dimensiones de la pantalla y las celdas
TAMANO_VENTANA = 700
TAMANO_CELDA = TAMANO_VENTANA // len(MAPA)


#personas en el tablero
CANTIDAD_PERSONAS = 10

#elementos del tablero

FONDO = 'TEMPLATES/map.png'
EDIFICIO = (128, 128, 128)#                     '#'
CAMINO = (255, 255, 255) #                      ' '
EMPEDRADO = 'TEMPLATES/b.png'#      '+'
OBSTACULO = 'TEMPLATES/cono.png'#   'o'
PERSONAS = 'TEMPLATES/p.png'#       'p'

AUTO_UP = 'TEMPLATES/u.png'
AUTO_DOWN = 'TEMPLATES/d.png'
AUTO_LEFT = 'TEMPLATES/l.png'
AUTO_DIGHT = 'TEMPLATES/r.png'


