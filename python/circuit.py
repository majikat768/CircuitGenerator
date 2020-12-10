#!/usr/bin/python

from constants import *
from Cell import Cell
from Wire import Wire

wires = []

for i in range(numCols):
    for j in range(numRows):
        cells.append(Cell(i,j))

numTries = 100
for i in range(numWires):
    tries = 0
    start = cells[random.randint(0,len(cells)-1)]
    while start.open is False:
        tries += 1
        if tries > numTries:
            break
        start = cells[random.randint(0,len(cells)-1)]
    wire = Wire(start)
    wire.create_wire()
    if len(wire.cells) > minLineLength:
        wires.append(wire)

def draw_grid():
    ctx.set_source_rgba(0,0,0,0.2)
    ctx.set_line_width(2)
    for i in range(numCols):
        ctx.move_to(i * cellSize,0)
        ctx.line_to(i * cellSize,numRows*cellSize)
        ctx.stroke()
    for j in range(numRows):
        ctx.move_to(0,j * cellSize)
        ctx.line_to(numCols*cellSize,j * cellSize)
        ctx.stroke()

ctx.rectangle(0,0,W,H)
ctx.set_source_rgb(BOARD_COL[0], BOARD_COL[1], BOARD_COL[2])
ctx.fill()
for wire in wires:
    wire.draw_wire()
    for fork in wire.forks:
        if fork.start != wire.cells[len(wire.cells) - 1]:
            fork.create_wire()
            if len(fork.cells) > 1:
                fork.draw_wire()
#draw_grid()
surface.write_to_png('./circuit.png')


