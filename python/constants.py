import cairo
import random
import numpy as np

directions = [
    (1,0),(1,1),
    (0,1),(-1,1),
    (-1,0),(-1,-1),
    (0,-1),(1,-1)
]

BOARD_COL = (0.09, 0.3, 0.09)
WIRE_COL = (0.6, 0.5, 0.25)
#WIRE_COL = (0.15, 0.35, 0.15)
HOLE_COL = (0,0,0)
cellSize = 20
numRows = 30
numCols = 40

lineLength = 100
forkLength = 5
minLineLength = 2
lineWidth = 5
numWires = 80

cells = []
W = cellSize * numCols
H = cellSize * numRows
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32,W,H)
ctx = cairo.Context(surface)


def get_cell(x,y):
    for c in cells:
        if c.x == x and c.y == y:   return c
    return None;
